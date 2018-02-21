import random

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from kivy.core.window import Window
from kivy.clock import Clock


SCALE = .75


class Bird(Widget):
    velocity_y = 0
    gravity = -9.8 * SCALE * 60          # (close enough to 9.8 as counts)

    def update(self, dt):
        self.velocity_y += self.gravity * dt
        self.velocity_y = max(self.velocity_y, -20 * SCALE  * 60)
        self.y += self.velocity_y * dt

    def on_touch_down(self, *ignore):
        self.velocity_y = 5 * SCALE  * 60


class Background(Widget):
    image = ObjectProperty(None)
    image_dupe = ObjectProperty(None)

    velocity_x = -2 * 60
    image_x = None
    image_dupe_x = None

    def update(self, dt):
        if self.image_x is None:
            self.image_x = self.image.x
            self.image_dupe_x = self.image_x + self.image.width
        self.image_x += self.velocity_x * dt
        self.image_dupe_x += self.velocity_x * dt

        self.image.x = int(self.image_x)
        self.image_dupe.x = int(self.image_dupe_x)

        if self.image.right <= 0:
            self.image_x = self.image.x = 0
            self.image_dupe_x = self.image_dupe.x = self.image.width


class Ground(Widget):
    velocity_x = -2 * 60
    image_x = 0
    ground_repeat = 24

    def update(self, dt):
        self.image_x += self.velocity_x * dt
        if self.image_x < -self.ground_repeat:
            self.image_x += self.ground_repeat
        self.x = int(self.image_x)


class Pipe(Widget):
    top_image = ObjectProperty(None)
    bottom_image = ObjectProperty(None)
    velocity_x = -2 * 60
    pos_x = None

    def update(self, dt):
        if self.pos_x is None:
            self.pos_x = self.x
        self.pos_x += self.velocity_x * dt
        self.x = int(self.pos_x)
        if self.right < 0:
            self.parent.remove_widget(self)


class Pipes(Widget):
    def update(self, dt):
        for child in list(self.children):
            child.update(dt)


class Game(Widget):
    background = ObjectProperty(None)
    bird = ObjectProperty(None)
    pipes = ObjectProperty(None)
    ground = ObjectProperty(None)
    score = NumericProperty(0)
    game_over_label = ObjectProperty(None)
    last_pipe = 0
    game_over = False

    def _on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(Menu())

    def update(self, dt):
        if self.game_over:
            return

        if dt > 1/30.:
            dt = 1/30.
        self.background.update(dt)
        self.bird.update(dt)
        self.pipes.update(dt)
        self.ground.update(dt)

        self.last_pipe -= dt
        if self.last_pipe < 0:
            pipe = Pipe(pos=(self.width,
                random.randint(self.ground.height + 50, self.height - 50 - 2.5 * 36)))
            pipe.scored = False
            self.pipes.add_widget(pipe)
            self.last_pipe = 5

        if self.bird.image.collide_widget(self.ground.image):
            self.game_over = True

        for pipe in self.pipes.children:
            if not pipe.scored and pipe.right < self.bird.x:
                pipe.scored = True
                self.score += 1
            if pipe.top_image.collide_widget(self.bird.image):
                self.game_over = True
            elif pipe.bottom_image.collide_widget(self.bird.image):
                self.game_over = True

        if self.game_over:
            self.game_over_label.opacity = 1.0
            self.bind(on_touch_down=self._on_touch_down)



class Menu(Widget):
    background = ObjectProperty(None)
    ground = ObjectProperty(None)

    def on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        game = Game()
        parent.add_widget(game)
        Clock.schedule_interval(game.update, 1.0/60.0)


class Top(Widget):
    pass


class GameApp(App):
    def build(self):
        top = Top()
        menu = Menu()
        top.add_widget(menu)
        Window.size = menu.size
        return top


if __name__ == '__main__':
    from game import GameApp
    GameApp().run()
