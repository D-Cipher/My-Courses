# this code originally was https://github.com/grierson/breakout-kivy

import math
import random

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import (ListProperty, NumericProperty,
                             ObjectProperty, StringProperty)
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.window import Window

from kivyparticle import ParticleSystem

__version__ = '0.1'


class Graphic(Widget):
    scale = NumericProperty(1)
    rotate = NumericProperty(0)


class Game(FloatLayout):
    blocks = ListProperty([])
    player = ObjectProperty()
    ball = ObjectProperty()
    border_left = ObjectProperty()
    border_right = ObjectProperty()
    border_top = ObjectProperty()

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1./60.)
        Window.bind(on_key_down=self.on_key_down)
        self.reset()

    def setup_blocks(self):
        for y_jump in range(5):
            for x_jump in range(10):
                if self.drop:
                    block = Block(0.05 + 0.09*x_jump, 1 + 0.05*y_jump)
                    duration = .5
                    if self.random:
                        duration = random.random() / 2
                    Animation(pos_hint_y=0.65 + 0.05*y_jump, t=self.drop, duration=duration).start(block)
                else:
                    block = Block(0.05 + 0.09*x_jump, 0.65 + 0.05*y_jump)
                if self.proper_colors:
                    block.color = block.proper_color
                self.blocks.append(block)
                self.add_widget(block)

    def start(self, *ignore):
        self.running = True

    def reset(self):
        self.running = False
        for block in self.blocks:
            self.remove_widget(block)
        self.blocks = []
        self.setup_blocks()
        self.ball.velocity = [random.random()-0.4, 0.4]
        self.ball.pos_hint_x = 0.5
        self.ball.pos_hint_y = 0.3
        self.player.position = 0.5
        self.do_layout()
        Clock.schedule_once(self.start, 2)

    drop = ''
    random = False
    block_react = False
    proper_colors = False
    anim_block_remove = False
    particles = False
    def on_key_down(self, window, scancode, keycode, char, modifiers):
        if char == 'r':
            self.reset()
        if char == 'c':
            self.toggle_colors()
        elif char == '0':
            self.drop = ''
            self.reset()
        elif char == '1':
            self.drop = 'linear'
            self.reset()
        elif char == '2':
            self.drop = 'out_quad'
            self.reset()
        elif char == '3':
            self.drop = 'out_bounce'
            self.reset()
        elif char == '4':
            self.drop = 'out_elastic'
            self.reset()
        elif char == '5':
            self.random = not self.random
            self.reset()
        elif char == '6':
            self.ball.react = not self.ball.react
        elif char == '7':
            self.ball.turn = not self.ball.turn
        elif char == '8':
            self.ball.trail = not self.ball.trail
        elif char == '9':
            self.block_react = not self.block_react
        elif char == 'b':
            self.anim_block_remove = not self.anim_block_remove
        elif char == 'e':
            self.player.toggle_eyes()
        elif char == 'f':
            self.player.eyes_follow = not self.player.eyes_follow
        elif char == 'p':
            self.particles = not self.particles

    def toggle_colors(self):
        self.proper_colors = not self.proper_colors
        if self.proper_colors:
            self.player.color = self.player.proper_color
            self.ball.color = self.ball.proper_color
            for block in self.blocks:
                block.color = block.proper_color
            self.border_left.color = self.border_left.proper_color
            self.border_right.color = self.border_right.proper_color
            self.border_top.color = self.border_top.proper_color
        else:
            self.player.color = self.ball.color = [1, 1, 1, 1]
            for block in self.blocks:
                block.color = [1, 1, 1, 1]
            self.border_left.color = [1, 1, 1, 1]
            self.border_right.color = [1, 1, 1, 1]
            self.border_top.color = [1, 1, 1, 1]

    def destroy_blocks(self, ball):
        for i, block in enumerate(self.blocks):
            if block.collide_widget(ball):
                y_overlap = (
                    ball.top - block.y if ball.velocity[1] > 0
                    else block.top - ball.y) / block.size_hint_y
                x_overlap = (
                    ball.right - block.x if ball.velocity[0] > 0
                    else block.right - ball.x) / block.size_hint_x
                if x_overlap < y_overlap:
                    ball.velocity[0] *= -1
                else:
                    ball.velocity[1] *= -1

                if self.anim_block_remove:
                    a = Animation(scale=.1, color=[1, 0, 0, 0], t='out_quad', duration=.5)
                    a.bind(on_complete=lambda a, w: self.remove_widget(w))
                    a.start(block)
                else:
                    self.remove_widget(block)

                if self.particles:
                    explode = ParticleSystem('particle.pex')
                    explode.emitter_x = ball.x
                    explode.emitter_y = ball.y
                    self.add_widget(explode)
                    explode.start(duration=.2)
                    Clock.schedule_once(lambda *a: self.remove_widget(explode), 1)

                del self.blocks[i]

                return True

    def update(self, dt):
        if not self.running:
            return
        self.ball.update(dt)
        self.player.update(dt)

    def game_bounce(self):
        if not self.block_react:
            return
        for block in self.blocks:
            block.rotate = 10 * (random.random()-.5)
            Animation(rotate=0, duration=.05, t='out_bounce').start(block)
            block.scale = 1 + (random.random() - .5)/8
            Animation(scale=1, duration=.05, t='out_bounce').start(block)


class Eye(Widget):
    scale = NumericProperty(1)
    rotate = NumericProperty(0)


class Player(Graphic):
    position = NumericProperty(0.5)
    color = ListProperty([1, 1, 1, 1])
    proper_color = [.3, .8, .3, 1]

    def on_touch_move(self, touch):
        self.position = touch.sx

    eyes_enabled = False
    eyes_follow = False
    def toggle_eyes(self):
        self.eyes_enabled = not self.eyes_enabled
        if self.eyes_enabled:
            self.eye_left = Eye(right=self.x + 5, y=self.y, size=(self.height, self.height))
            self.add_widget(self.eye_left)
            self.eye_right = Eye(right=self.right - 5, y=self.y, size=(self.height, self.height))
            self.add_widget(self.eye_right)
        else:
            self.remove_widget(self.eye_left)
            self.remove_widget(self.eye_right)
            self.eye_left = self.eye_right = None

    def update(self, dt):
        if self.eyes_enabled:
            bx, by = self.parent.ball.center
            if self.eyes_follow:
                ex, ey = self.eye_left.center
                self.eye_left.rotate = math.atan2(by-ey, bx-ex) * 90 / (math.pi / 2) - 90
                ex, ey = self.eye_right.center
                self.eye_right.rotate = math.atan2(by-ey, bx-ex) * 90 / (math.pi / 2) - 90
            self.eye_left.x = self.x + 5
            self.eye_right.right = self.right - 5


class Ball(Graphic):
    pos_hint_x = NumericProperty(0.5)
    pos_hint_y = NumericProperty(0.3)
    side_size = NumericProperty(0.)
    velocity = ListProperty([0.1, 0.5])
    color = ListProperty([1, 1, 1, 1])
    proper_color = [.8, .8, .3, 1]

    react = False
    turn = False
    trail = False
    trail_time = 0
    trail_widget = None

    def update(self, dt):
        self.pos_hint_x += self.velocity[0] * dt
        self.pos_hint_y += self.velocity[1] * dt
        bounce = False
        if self.parent.border_right.collide_widget(self):
            self.velocity[0] = -(abs(self.velocity[0]))
            self.right = self.parent.border_right.x
            bounce = True
        elif self.parent.border_left.collide_widget(self):
            self.velocity[0] = abs(self.velocity[0])
            self.x = self.parent.border_left.right
            bounce = True
        elif self.parent.border_top.collide_widget(self):
            self.velocity[1] = -abs(self.velocity[1])
            self.top = self.parent.border_top.y
            bounce = True
        elif self.y < 0:
            self.velocity[1] = abs(self.velocity[1])
            self.pos_hint_y = 0
            bounce = True
        bounce = self.bounce_from_player(self.parent.player) or bounce
        bounce = self.parent.destroy_blocks(self) or bounce
        if bounce:
            self.parent.game_bounce()
            if self.react:
                Animation.cancel_all(self)
                self.scale = 1.5
                Animation(scale=1, t='out_bounce', duration=.1).start(self)
                self.color = [1, 1, 1, 1]
                Animation(color=[.8, .8, .3, 1], duration=.05).start(self)

        direction = math.atan2(self.velocity[1], self.velocity[0]) * 90 / (math.pi / 2)
        if self.turn:
            self.rotate = direction

        self.parent.do_layout()

        if self.trail:
            if self.trail_widget is None:
                self.trail_widget = Trail()
                self.trail_widget.width = self.width * .3
                self.add_widget(self.trail_widget)
                self.trail_time = .1
            if self.trail_time < 0:
                self.trail_widget.add(self.center, direction, self.side_size * .5)
                self.trail_time = .01
            else:
                self.trail_time -= dt
        elif self.trail_widget:
            self.remove_widget(self.trail_widget)
            self.trail_widget = None

    def bounce_from_player(self, player):
        if player.collide_widget(self):
            self.velocity[1] = abs(self.velocity[1])
            self.velocity[0] += 0.1 * ((self.center_x - player.center_x) / player.width)
            return True


class TrailBit(Widget):
    color = ListProperty([.8, .8, .3, 1])
    quad = ListProperty([0] * 8)
    end = ListProperty([0, 0])

    def __init__(self, quad):
        super(TrailBit, self).__init__()
        self.quad = quad


class Trail(Widget):
    last = None
    last_points = None

    def add(self, point, direction, width):
        point = list(point)
        if self.last is None:
            self.last = point
            return
        sx, sy = self.last
        ex, ey = point

        # figure out the normalised normal vector to the trail line
        dx = ex - sx
        dy = ey - sy
        dx, dy = dy, -dx
        l = math.sqrt((dx * dx) + (dy * dy))
        ndx = dx / l
        ndy = dy / l

        # scale by trail width and calculate points
        ox = ndx * width / 2
        oy = ndy * width / 2

        if self.last_points is None:
            x1 = sx - ox
            y1 = sy - oy
            x2 = sx + ox
            y2 = sy + oy
        else:
            x1, y1, x2, y2 = self.last_points

        x3 = ex + ox
        y3 = ey + oy
        x4 = ex - ox
        y4 = ey - oy
        self.last_points = (x4, y4, x3, y3)

        bit = TrailBit((x1, y1, x2, y2, x3, y3, x4, y4))
        a = Animation(color=[.8, 0, 0, 0], duration=0.5)
        a.bind(on_complete=lambda a, w: self.remove_widget(w))
        a.start(bit)
        self.add_widget(bit)
        self.last = point


class Border(Graphic):
    color = ListProperty([1, 1, 1, 1])
    proper_color = [.5, .1, .1, 1]


class Block(Graphic):
    pos_hint_x = NumericProperty(0)
    pos_hint_y = NumericProperty(0)
    color = ListProperty([1, 1, 1, 1])
    proper_color = [.6, .3, .1, 1]

    def __init__(self, x, y):
        super(Block, self).__init__()
        self.pos_hint_x = x
        self.pos_hint_y = y


class BreakoutApp(App):
    def build(self):
        return Game()

BreakoutApp().run()
