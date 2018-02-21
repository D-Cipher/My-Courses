# platformer tileset artwork from
# http://www.reddit.com/r/gamedev/comments/1iavnq/300_platformer_tiles_sprites_for_use_in_your_game/

from kivy.app import App
from kivy.core.window import Window

import tmx


class MyMap(tmx.TileMapWidget):
    def on_touch_down(self, touch):
        self.touch_start_focus = self.map.viewport.center

    def on_touch_move(self, touch):
        fx, fy = self.touch_start_focus
        self.set_focus(fx + touch.ox - touch.x, fy + touch.oy - touch.y)


class PlatformerApp(App):
    def build(self):
        scale = Window.height / 252.     # cell size 21px * 12 high
        return MyMap('images/platformer.tmx', Window.size, scale)

PlatformerApp().run()
