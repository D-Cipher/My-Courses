# platformer tileset artwork from
# http://www.reddit.com/r/gamedev/comments/1iavnq/300_platformer_tiles_sprites_for_use_in_your_game/

from collections import defaultdict

from kivy.app import App
from kivy.core.window import Window, Keyboard
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.metrics import sp
from kivy.clock import Clock
from kivy.utils import platform

import tmx
from rect import Rect
from kivy_fix import SpriteAtlas


keys = defaultdict(lambda: False)


class Sprite(Image):
    def __init__(self, **kwargs):
        super(Sprite, self).__init__(allow_stretch=True, **kwargs)
        self.texture.mag_filter = 'nearest'
        w, h = self.texture_size
        self.size = (params.scale * w, params.scale * h)


class Player(Sprite):
    def __init__(self, pos, map):
        self.map = map
        self.images = SpriteAtlas('images/tiles.atlas')
        super(Player, self).__init__(pos=pos, texture=self.images['player'])
        self.resting = False
        self.dy = 0

    def update(self):
        last = Rect(*(self.pos + self.size))

        dx = 0
        if keys.get(Keyboard.keycodes['left']):
            dx -= 2 * params.scale
        if keys.get(Keyboard.keycodes['right']):
            dx += 2 * params.scale
        if keys.get(Keyboard.keycodes['spacebar']) and self.resting:
            self.dy = 9 * params.scale
            self.resting = False

        self.dy = max(-8 * params.scale, self.dy - .5 * params.scale)

        self.x += dx
        self.y += self.dy

        new = Rect(*(self.pos + self.size))
        for cell in self.map.layers['objects'].collide(new, 'blocker'):
            blocker = cell['blocker']
            if 'l' in blocker and last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if 'r' in blocker and last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if 't' in blocker and last.bottom >= cell.top and new.bottom < cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if 'b' in blocker and last.top <= cell.bottom and new.top > cell.bottom:
                new.top = cell.bottom
                self.dy = 0
        self.pos = new.bottomleft


class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.map = tmx.TileMapWidget('images/platformer.tmx', Window.size, params.scale)
        self.add_widget(self.map)
        spawn = self.map.map.layers['objects'].find('spawn')[0]
        self.player = Player((spawn.px, spawn.py), self.map.map)
        self.map.add_widget(self.player)        # add to map so it's scrolled
        Clock.schedule_interval(self.update, 1.0/60.0)

        if True: #platform() == 'android':
            self.left_button = Image(allow_stretch=True, source='images/left-arrow-button.png',
                                     size=(sp(60), sp(60)), pos=(sp(10), sp(10)))
            self.add_widget(self.left_button)
            self.right_button = Image(allow_stretch=True, source='images/right-arrow-button.png',
                                     size=(sp(60), sp(60)), pos=(sp(80), sp(10)))
            self.add_widget(self.right_button)
            self.jump_button = Image(allow_stretch=True, source='images/up-arrow-button.png',
                                     size=(sp(60), sp(60)), pos=(Window.width - sp(70), sp(10)))
            self.add_widget(self.jump_button)

    def update(self, *ignore):
        self.player.update()
        self.map.set_focus(*self.player.pos)

    def on_touch_down(self, touch):
        if self.left_button.collide_point(touch.x, touch.y):
            keys[Keyboard.keycodes['left']] = True
        elif self.right_button.collide_point(touch.x, touch.y):
            keys[Keyboard.keycodes['right']] = True
        elif self.jump_button.collide_point(touch.x, touch.y):
            keys[Keyboard.keycodes['spacebar']] = True

    def on_touch_up(self, touch):
        if self.left_button.collide_point(touch.ox, touch.oy):
            keys[Keyboard.keycodes['left']] = False
        elif self.right_button.collide_point(touch.ox, touch.oy):
            keys[Keyboard.keycodes['right']] = False
        elif self.jump_button.collide_point(touch.ox, touch.oy):
            keys[Keyboard.keycodes['spacebar']] = False


class PlatformerApp(App):
    def build(self):
        params.init()
        return Game()


class params(object):
    def init(self):
        self.width, self.height = Window.size
        self.scale = self.height / 252.      # 21 tile size * 12
params = params()


if __name__ == '__main__':
    if platform() != 'android':
        def on_key_down(window, keycode, *rest):
            keys[keycode] = True
        def on_key_up(window, keycode, *rest):
            keys[keycode] = False
        Window.bind(on_key_down=on_key_down, on_key_up=on_key_up)
    PlatformerApp().run()
