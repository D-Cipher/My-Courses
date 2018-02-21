# "Tiled" TMX loader/renderer and more
# Copyright 2012 Richard Jones <richard@mechanicalcat.net>
# This code is placed in the Public Domain.

# TODO: support properties on more things

import os
import sys
import struct
from xml.etree import ElementTree
from rect import Rect

import kivy

kivy.require('1.8.0')

from kivy.uix.image import Image
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
from kivy.graphics import Translate, PushMatrix, PopMatrix
from kivy.utils import get_color_from_hex


class Tile(object):
    '''
    Tiles are NOT SCALED, but do record the scaled tile dimensions.
    '''

    def __init__(self, gid, texture, tileset):
        self.gid = gid
        self.texture = texture
        self.tile_width = tileset.tile_width
        self.tile_height = tileset.tile_height
        self.scaled_tile_width = tileset.scaled_tile_width
        self.scaled_tile_height = tileset.scaled_tile_height
        self.properties = {}
        self.scale = tileset.scale

    def loadxml(self, tag):
        props = tag.find('properties')
        if props is None:
            return
        for c in props.findall('property'):
            # store additional properties.
            name = c.attrib['name']
            value = c.attrib['value']

            # TODO hax
            if value.isdigit():
                value = int(value)
            self.properties[name] = value

    def __repr__(self):
        return '<Tile %d>' % self.gid


class Tileset(object):
    '''
    Tile sets are NOT SCALED, but do record the scaled tile dimensions.
    '''

    def __init__(self, name, tile_width, tile_height, firstgid, spacing=0, margin=0, scale=1):
        self.name = name
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.firstgid = firstgid
        self.spacing = spacing
        self.margin = margin
        self.tiles = []
        self.properties = {}
        self.scale = scale
        self.scaled_tile_width = self.tile_width * self.scale
        self.scaled_tile_height = self.tile_height * self.scale

    @classmethod
    def fromxml(cls, tag, tilemap, firstgid=None):
        if 'source' in tag.attrib:
            firstgid = int(tag.attrib['firstgid'])
            path = tag.attrib['source']
            if not os.path.exists(path):
                path = os.path.join(tilemap.file_path, path)
            with open(path) as f:
                tileset = ElementTree.fromstring(f.read())
            return cls.fromxml(tileset, firstgid)

        name = tag.attrib['name']
        if firstgid is None:
            firstgid = int(tag.attrib['firstgid'])
        tile_width = int(tag.attrib['tilewidth'])
        tile_height = int(tag.attrib['tileheight'])
        spacing = int(tag.get('spacing', 0))
        margin = int(tag.get('margin', 0))

        tileset = cls(name, tile_width, tile_height, firstgid,
                      spacing, margin, tilemap.scale)

        for c in tag.getchildren():
            if c.tag == "image":
                # create a tileset
                tileset.add_image(tilemap.file_path, c.attrib['source'])
            elif c.tag == 'tile':
                gid = tileset.firstgid + int(c.attrib['id'])
                tileset.get_tile(gid).loadxml(c)
        return tileset

    def add_image(self, base_path, file):
        if not os.path.exists(file):
            file = os.path.join(base_path, file)
        texture = Image(source=file).texture
        texture.mag_filter = 'nearest'
        if texture is None:
            sys.exit('failed to locate image file %r' % file)

        id = self.firstgid
        th = self.tile_height + self.spacing
        tw = self.tile_width + self.spacing
        for j in xrange(texture.height / th):
            for i in xrange(texture.width / tw):
                x = (i * tw) + self.margin
                # convert the y coordinate to OpenGL (0 at bottom of texture)
                y = texture.height - ((j + 1) * th)
                tile = texture.get_region(x, y, self.tile_width, self.tile_height)
                self.tiles.append(Tile(id, tile, self))
                id += 1

    def get_tile(self, gid):
        return self.tiles[gid - self.firstgid]


class Tilesets(dict):
    def add(self, tileset):
        for i, tile in enumerate(tileset.tiles):
            i += tileset.firstgid
            self[i] = tile


class Cell(object):
    '''Layers are made of Cells (or empty space).

    Cell pixel coordinates and dimensions are ALWAYS SCALED.

    Cells have some basic properties:

    x, y - the cell's index in the layer
    px, py - the cell's pixel position
    left, right, top, bottom - the cell's pixel boundaries

    Additionally the cell may have other properties which are accessed using
    standard dictionary methods:

       cell['property name']

    You may assign a new value for a property to or even delete an existing
    property from the cell - this will not affect the Tile or any other Cells
    using the Cell's Tile.
    '''

    def __init__(self, x, y, px, py, tile):
        self.map_px = px
        self.map_py = py
        self.x, self.y = x, y
        self.px, self.py = px, py
        self.px_width, self.px_height = tile.scaled_tile_width, tile.scaled_tile_height
        self.tile = tile
        self.bottomleft = (px, py)
        self.left = px
        self.right = px + self.px_width
        self.bottom = py
        self.top = py + self.px_height
        self.center = (px + self.px_width // 2, py + self.px_height // 2)
        self._added_properties = {}
        self._deleted_properties = set()

    def __repr__(self):
        return '<Cell %s,%s %d>' % (self.px, self.py, self.tile.gid)

    def __contains__(self, key):
        if key in self._deleted_properties:
            return False
        return key in self._added_properties or key in self.tile.properties

    def __getitem__(self, key):
        if key in self._deleted_properties:
            raise KeyError(key)
        if key in self._added_properties:
            return self._added_properties[key]
        if key in self.tile.properties:
            return self.tile.properties[key]
        raise KeyError(key)

    def __setitem__(self, key, value):
        self._added_properties[key] = value

    def __delitem__(self, key):
        self._deleted_properties.add(key)

    def intersects(self, other):
        '''Determine whether this Cell intersects with the other rect (which has
        .x, .y, .width and .height attributes.)
        '''
        if self.px + self.px_width < other.x:
            return False
        if other.x + other.width < self.px:
            return False
        if self.py + self.px_height < other.y:
            return False
        if other.y + other.height < self.py:
            return False
        return True


class LayerIterator(object):
    '''Iterates over all the cells in a layer in column,row order.
    '''

    def __init__(self, layer):
        self.layer = layer
        self.i, self.j = 0, 0

    def next(self):
        if self.i == self.layer.width:
            self.j += 1
            self.i = 0
        if self.j == self.layer.height:
            raise StopIteration()
        value = self.layer[self.i, self.j]
        self.i += 1
        return value


class Layer(object):
    '''A 2d grid of Cells.

    Layer pixel positions and dimensions are ALWAYS SCALED.

    Layers have some basic properties:

        width, height - the dimensions of the Layer in cells
        tile_width, tile_height - the dimensions of each cell
        px_width, px_height - the dimensions of the Layer in pixels
        tilesets - the tilesets used in this Layer (a Tilesets instance)
        properties - any properties set for this Layer
        cells - a dict of all the Cell instances for this Layer, keyed off
                (x, y) index.

    Additionally you may look up a cell using direct item access:

       layer[x, y] is layer.cells[x, y]

    Note that empty cells will be set to None instead of a Cell instance.
    '''

    def __init__(self, name, visible, map):
        self.name = name
        self.visible = visible
        self.position = (0, 0)
        self.px_width = map.scaled_width
        self.px_height = map.scaled_height
        self.tile_width = map.scaled_tile_width
        self.tile_height = map.scaled_tile_height
        self.width = map.width
        self.height = map.height
        self.tilesets = map.tilesets
        self.properties = {}
        self.cells = {}

    def __repr__(self):
        return '<Layer "%s" at 0x%x>' % (self.name, id(self))

    def __getitem__(self, pos):
        return self.cells.get(pos)

    def __setitem__(self, pos, tile):
        x, y = pos
        px = x * self.tile_width
        py = y * self.tile_width
        self.cells[pos] = Cell(x, y, px, py, tile)

    def __iter__(self):
        return LayerIterator(self)

    @classmethod
    def fromxml(cls, tag, map):
        layer = cls(tag.attrib['name'], int(tag.attrib.get('visible', 1)), map)

        data = tag.find('data')
        if data is None:
            raise ValueError('layer %s does not contain <data>' % layer.name)

        data = data.text.strip()
        data = data.decode('base64').decode('zlib')
        data = struct.unpack('<%di' % (len(data) / 4,), data)
        assert len(data) == layer.width * layer.height, "data len (%d) != width (%d) x height (%d)" % (
        len(data), layer.width, layer.height)
        for i, gid in enumerate(data):
            if gid < 1: continue  # not set
            tile = map.tilesets[gid]
            x = i % layer.width
            y = i // layer.width
            layer.cells[x, y] = Cell(x, y, x * layer.tile_width, y * layer.tile_height, tile)

        return layer

    def update(self, dt, *args):
        pass

    def set_view(self, x, y, w, h, viewport_ox=0, viewport_oy=0):
        self.view_x, self.view_y = x, y
        self.view_w, self.view_h = w, h
        x -= viewport_ox
        y -= viewport_oy
        self.position = (x, y)

    def find(self, *properties):
        '''Find all cells with the given properties set.
        '''
        r = []
        for propname in properties:
            for cell in self.cells.values():
                if cell and propname in cell:
                    r.append(cell)
        return r

    def match(self, **properties):
        '''Find all cells with the given properties set to the given values.
        '''
        r = []
        for propname in properties:
            for cell in self.cells.values():
                if propname not in cell:
                    continue
                if properties[propname] == cell[propname]:
                    r.append(cell)
        return r

    def collide(self, rect, propname):
        '''Find all cells the rect is touching that have the indicated property
        name set.
        '''
        r = []
        for cell in self.get_in_region(rect.left, rect.bottom, rect.right,
                                       rect.top):
            if not cell.intersects(rect):
                continue
            if propname in cell:
                r.append(cell)
        return r

    def get_in_region(self, x1, y1, x2, y2):
        '''Return cells (in [column][row]) that are within the map-space
        pixel bounds specified by the bottom-left (x1, y1) and top-right
        (x2, y2) corners.

        Return a list of Cell instances.
        '''
        i1 = max(0, x1 // self.tile_width)
        j1 = max(0, y1 // self.tile_height)
        i2 = min(self.width, x2 // self.tile_width + 1)
        j2 = min(self.height, y2 // self.tile_height + 1)
        return [self.cells[i, j]
                for i in range(int(i1), int(i2))
                for j in range(int(j1), int(j2))
                if (i, j) in self.cells]

    def get_at(self, x, y):
        '''Return the cell at the nominated (x, y) coordinate.

        Return a Cell instance or None.
        '''
        i = x // self.tile_width
        j = y // self.tile_height
        return self.cells.get((i, j))

    def neighbors(self, index):
        '''Return the indexes of the valid (ie. within the map) cardinal (ie.
        North, South, East, West) neighbors of the nominated cell index.

        Returns a list of 2-tuple indexes.
        '''
        i, j = index
        n = []
        if i < self.width - 1:
            n.append((i + 1, j))
        if i > 0:
            n.append((i - 1, j))
        if j < self.height - 1:
            n.append((i, j + 1))
        if j > 0:
            n.append((i, j - 1))
        return n


class Object(object):
    '''An object in a TMX object layer.

    Object pixel positions and dimensions are ALWAYS SCALED

        name: The name of the object. An arbitrary string.
        type: The type of the object. An arbitrary string.
        x: The x coordinate of the object in pixels.
        y: The y coordinate of the object in pixels.
        width: The width of the object in pixels (defaults to 0).
        height: The height of the object in pixels (defaults to 0).
        gid: An reference to a tile (optional).
        visible: Whether the object is shown (1) or hidden (0). Defaults to 1.
    '''

    def __init__(self, type, x, y, width=0, height=0, name=None,
                 gid=None, tile=None, visible=1):
        self.type = type
        self.px = x
        self.left = x
        if tile:
            y -= tile.scaled_tile_height
            width = tile.scaled_tile_width
            height = tile.scaled_tile_height
        self.py = y
        self.bottom = y
        self.width = width
        self.right = x + width
        self.height = height
        self.top = y + height
        self.name = name
        self.gid = gid
        self.tile = tile
        self.visible = visible
        self.properties = {}

        self._added_properties = {}
        self._deleted_properties = set()

    def __repr__(self):
        if self.tile:
            return '<Object %s,%s %s,%s tile=%d>' % (self.px, self.py, self.width, self.height, self.gid)
        else:
            return '<Object %s,%s %s,%s>' % (self.px, self.py, self.width, self.height)

    def __contains__(self, key):
        if key in self._deleted_properties:
            return False
        if key in self._added_properties:
            return True
        if key in self.properties:
            return True
        return self.tile and key in self.tile.properties

    def __getitem__(self, key):
        if key in self._deleted_properties:
            raise KeyError(key)
        if key in self._added_properties:
            return self._added_properties[key]
        if key in self.properties:
            return self.properties[key]
        if self.tile and key in self.tile.properties:
            return self.tile.properties[key]
        raise KeyError(key)

    def __setitem__(self, key, value):
        self._added_properties[key] = value

    def __delitem__(self, key):
        self._deleted_properties.add(key)

    @classmethod
    def fromxml(cls, tag, map):
        if 'gid' in tag.attrib:
            gid = int(tag.attrib['gid'])
            tile = map.tilesets[gid]
            w = tile.tile_width
            h = tile.tile_height
        else:
            gid = None
            tile = None
            w = int(tag.attrib['width']) * map.scale
            h = int(tag.attrib['height']) * map.scale
            x = int(tag.attrib['x']) * map.scale
            y = map.scaled_height - h - int(tag.attrib['y']) * map.scale

        o = cls(tag.attrib.get('type', 'rect'), x, y, w, h, tag.attrib.get('name'), gid, tile,
                int(tag.attrib.get('visible', 1)))

        props = tag.find('properties')
        if props is None:
            return o

        for c in props.findall('property'):
            # store additional properties.
            name = c.attrib['name']
            value = c.attrib['value']

            # TODO hax
            if value.isdigit():
                value = int(value)
            o.properties[name] = value
        return o

    def intersects(self, x1, y1, x2, y2):
        if x2 < self.px:
            return False
        if y2 < self.py:
            return False
        if x1 > self.px + self.width:
            return False
        if y1 > self.py + self.height:
            return False
        return True


class ObjectLayer(object):
    '''A layer composed of basic primitive shapes.

    Actually encompasses a TMX <objectgroup> but even the TMX documentation
    refers to them as object layers, so I will.

    ObjectLayers have some basic properties:

        position - ignored (cannot be edited in the current Tiled editor)
        name - the name of the object group.
        color - the color used to display the objects in this group.
        opacity - the opacity of the layer as a value from 0 to 1.
        visible - whether the layer is shown (1) or hidden (0).
        objects - the objects in this Layer (Object instances)
    '''
    def __init__(self, name, color, objects, opacity=1,
                 visible=1, position=(0, 0)):
        self.name = name
        self.color = color
        self.objects = objects
        self.opacity = opacity
        self.visible = visible
        self.position = position
        self.properties = {}

    def __repr__(self):
        return '<ObjectLayer "%s" at 0x%x>' % (self.name, id(self))

    def __iter__(self):
        return iter(self.objects)

    @classmethod
    def fromxml(cls, tag, map):
        layer = cls(tag.attrib['name'], tag.attrib.get('color'), [],
                    float(tag.attrib.get('opacity', 1)),
                    int(tag.attrib.get('visible', 1)))
        for object in tag.findall('object'):
            layer.objects.append(Object.fromxml(object, map))
        for c in tag.findall('property'):
            # store additional properties.
            name = c.attrib['name']
            value = c.attrib['value']

            # TODO hax
            if value.isdigit():
                value = int(value)
            layer.properties[name] = value
        return layer

    def update(self, dt, *args):
        pass

    def set_view(self, x, y, w, h, viewport_ox=0, viewport_oy=0):
        self.view_x, self.view_y = x, y
        self.view_w, self.view_h = w, h
        x -= viewport_ox
        y -= viewport_oy
        self.position = (x, y)

    def find(self, *properties):
        '''Find all cells with the given properties set.
        '''
        r = []
        for propname in properties:
            for object in self.objects:
                if object and propname in object or propname in self.properties:
                    r.append(object)
        return r

    def match(self, **properties):
        '''Find all objects with the given properties set to the given values.
        '''
        r = []
        for propname in properties:
            for object in self.objects:
                if propname in object:
                    val = object[propname]
                elif propname in self.properties:
                    val = self.properties[propname]
                else:
                    continue
                if properties[propname] == val:
                    r.append(object)
        return r

    def collide(self, rect, propname):
        '''Find all objects the rect is touching that have the indicated
        property name set.
        '''
        r = []
        for object in self.get_in_region(rect.left, rect.bottom, rect.right,
                                         rect.top):
            if propname in object or propname in self.properties:
                r.append(object)
        return r

    def get_in_region(self, x1, y1, x2, y2):
        '''Return objects that are within the map-space
        pixel bounds specified by the bottom-left (x1, y1) and top-right
        (x2, y2) corners.

        Return a list of Object instances.
        '''
        return [obj for obj in self.objects if obj.intersects(x1, y1, x2, y2)]

    def get_at(self, x, y):
        '''Return the first object found at the nominated (x, y) coordinate.

        Return an Object instance or None.
        '''
        for object in self.objects:
            if object.contains(x, y):
                return object


class SpriteLayer(object):
    def __init__(self):
        super(SpriteLayer, self).__init__()
        self.visible = True

    def set_view(self, x, y, w, h, viewport_ox=0, viewport_oy=0):
        self.view_x, self.view_y = x, y
        self.view_w, self.view_h = w, h
        x -= viewport_ox
        y -= viewport_oy
        self.position = (x, y)


class Layers(list):
    def __init__(self):
        self.by_name = {}

    def add_named(self, layer, name):
        self.append(layer)
        self.by_name[name] = layer

    def __getitem__(self, item):
        if isinstance(item, int):
            return self[item]
        return self.by_name[item]


class TileMap(object):
    '''A TileMap is a collection of Layers which contain gridded maps or sprites
    which are drawn constrained by a viewport.

    And breathe.

    TileMaps are loaded from TMX files which sets the .layers and .tilesets
    properties. After loading additional SpriteLayers may be added.

    The tile map may be scaled from its original pixel dimensions using the
    scale parameter. This scales the artwork also.

    A TileMap's rendering is restricted by a viewport which is defined by the
    size passed in at construction time and the focus set by set_focus() or
    force_focus().

    TileMaps have a number of properties:

        width, height - the dimensions of the tilemap in cells
        tile_width, tile_height - the dimensions of the cells in the map
        px_width, px_height - the dimensions of the tilemap in pixels
        properties - any properties set on the tilemap in the TMX file
        layers - all layers of this tilemap as a Layers instance
        tilesets - all tilesets of this tilemap as a Tilesets instance
        fx, fy - viewport focus point
        view_w, view_h - viewport size
        view_x, view_y - viewport offset (origin)
        viewport - a Rect instance giving the current viewport specification

    '''

    def __init__(self, viewport_size, viewport_origin=(0, 0), scale=1):
        self.scale = scale
        self.px_width = self.scaled_width = 0
        self.px_height = self.scaled_height = 0
        self.tile_width = self.scaled_tile_width = 0
        self.tile_height = self.scaled_tile_height =0
        self.width = 0
        self.height = 0
        self.properties = {}
        self.layers = Layers()
        self.tilesets = Tilesets()
        self.fx, self.fy = 0, 0  # viewport focus point
        self.view_w, self.view_h = viewport_size  # viewport size
        self.view_x, self.view_y = viewport_origin  # viewport offset
        self.viewport = Rect(*(viewport_origin + viewport_size))

    @classmethod
    def load(cls, filename, viewport, scale=1):
        with open(filename) as f:
            map = ElementTree.fromstring(f.read())

        # get most general map information and create a surface
        tilemap = cls(viewport, scale=scale)
        tilemap.width = int(map.attrib['width'])
        tilemap.height = int(map.attrib['height'])
        tilemap.tile_width = int(map.attrib['tilewidth'])
        tilemap.tile_height = int(map.attrib['tileheight'])
        tilemap.px_width = tilemap.width * tilemap.tile_width
        tilemap.px_height = tilemap.height * tilemap.tile_height

        tilemap.file_path = os.path.dirname(filename)

        tilemap.scaled_width = tilemap.px_width * tilemap.scale
        tilemap.scaled_height = tilemap.px_height * tilemap.scale
        tilemap.scaled_tile_width = tilemap.tile_width * tilemap.scale
        tilemap.scaled_tile_height = tilemap.tile_height * tilemap.scale

        for tag in map.findall('tileset'):
            tilemap.tilesets.add(Tileset.fromxml(tag, tilemap))

        for tag in map.findall('layer'):
            layer = Layer.fromxml(tag, tilemap)
            tilemap.layers.add_named(layer, layer.name)

        for tag in map.findall('objectgroup'):
            layer = ObjectLayer.fromxml(tag, tilemap)
            tilemap.layers.add_named(layer, layer.name)

        return tilemap

    def update(self, dt, *args):
        for layer in self.layers:
            layer.update(dt, *args)

    _old_focus = None

    def set_focus(self, fx, fy, force=False):
        '''Determine the viewport based on a desired focus pixel in the
        Layer space (fx, fy) and honoring any bounding restrictions of
        child layers.

        The focus will always be shifted to ensure no child layers display
        out-of-bounds data, as defined by their dimensions px_width and px_height.
        '''
        # The result is that all chilren will have their viewport set, defining
        # which of their pixels should be visible.
        fx, fy = int(fx), int(fy)
        self.fx, self.fy = fx, fy

        a = (fx, fy)

        # check for NOOP (same arg passed in)
        if not force and self._old_focus == a:
            return
        self._old_focus = a

        # get our viewport information, scaled as appropriate
        w = int(self.view_w)
        h = int(self.view_h)
        w2, h2 = w // 2, h // 2

        if self.scaled_width <= w:
            # this branch for centered view and no view jump when
            # crossing the center; both when world width <= view width
            restricted_fx = self.scaled_width / 2
        else:
            if (fx - w2) < 0:
                restricted_fx = w2  # hit minimum X extent
            elif (fx + w2) > self.scaled_width:
                restricted_fx = self.scaled_width - w2  # hit maximum X extent
            else:
                restricted_fx = fx
        if self.scaled_height <= h:
            # this branch for centered view and no view jump when
            # crossing the center; both when world height <= view height
            restricted_fy = self.scaled_height / 2
        else:
            if (fy - h2) < 0:
                restricted_fy = h2  # hit minimum Y extent
            elif (fy + h2) > self.scaled_height:
                restricted_fy = self.scaled_height - h2  # hit maximum Y extent
            else:
                restricted_fy = fy

        # ... and this is our focus point, center of screen
        self.restricted_fx = int(restricted_fx)
        self.restricted_fy = int(restricted_fy)

        # determine child view bounds to match that focus point
        x, y = int(restricted_fx - w2), int(restricted_fy - h2)
        self.viewport.x = x
        self.viewport.y = y

        self.childs_ox = x - self.view_x
        self.childs_oy = y - self.view_y

        self.set_view(x, y, w, h)

    def force_focus(self, fx, fy):
        '''Force the manager to focus on a point, regardless of any managed layer
        visible boundaries.
        '''
        self.fx, self.fy = map(int, (fx, fy))

        # get our view size
        w = int(self.view_w)
        h = int(self.view_h)
        w2, h2 = w // 2, h // 2

        # bottom-left corner of the viewport
        x, y = fx - w2, fy - h2
        self.viewport.x = x
        self.viewport.y = y

        self.childs_ox = x - self.view_x
        self.childs_oy = y - self.view_y

        self.set_view(x, y, w, h)

    def set_view(self, x, y, w, h):
        for layer in self.layers:
            layer.set_view(x, y, w, h, self.view_x, self.view_y)

    def pixel_from_screen(self, x, y):
        '''Look up the Layer-space pixel matching the screen-space pixel.
        '''
        vx, vy = self.childs_ox, self.childs_oy
        return int(vx + x), int(vy + y)

    def pixel_to_screen(self, x, y):
        '''Look up the screen-space pixel matching the Layer-space pixel.
        '''
        screen_x = x - self.childs_ox
        screen_y = y - self.childs_oy
        return int(screen_x), int(screen_y)

    def index_at(self, x, y):
        '''Return the map index at the (screen-space) pixel position.
        '''
        sx, sy = self.pixel_from_screen(x, y)
        return int(sx // self.tile_width), int(sy // self.tile_height)


def load(filename, viewport, scale=1):
    return TileMap.load(filename, viewport, scale)


class TileMapWidget(Widget):
    def __init__(self, filename, viewport, scale):
        super(TileMapWidget, self).__init__()
        self.map = TileMap.load(filename, viewport, scale)
        self.size = (self.map.px_width, self.map.px_height)
        with self.canvas:
            for layer in self.map.layers:
                if hasattr(layer, 'color') and layer.color:
                    c = get_color_from_hex(layer.color)
                    c[-1] = .2
                    Color(*c)
                else:
                    Color(1, 1, 1)
                if not layer.visible:
                    continue
                for cell in layer:
                    if cell is None:
                        continue
                    x = cell.px
                    # OpenGL vs. TMX, y is reversed
                    y = self.map.scaled_height - cell.py - self.map.scaled_tile_height
                    if cell.tile:
                        texture = cell.tile.texture
                        size = cell.px_width, cell.px_height
                        Rectangle(pos=(x, y), texture=texture, size=size, allow_stretch=True)
                    else:
                        Rectangle(pos=(cell.px, cell.py), size=(cell.width, cell.height))
        self.set_focus(0, 0)

    def set_focus(self, x, y):
        self.map.set_focus(x, y)
        self._set_view()

    def force_focus(self, x, y):
        self.map.force_focus(x, y)
        self._set_view()

    def _set_view(self):
        fx, fy = self.map.viewport.origin
        # clear any previous before/after instructions
        self.canvas.before.clear()
        self.canvas.after.clear()
        with self.canvas.before:
            PushMatrix('projection_mat')
            Translate(-fx, -fy)
        with self.canvas.after:
            PopMatrix('projection_mat')
