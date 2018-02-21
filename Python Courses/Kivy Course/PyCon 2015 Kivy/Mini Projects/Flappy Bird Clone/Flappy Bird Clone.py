import random
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.logger import Logger
from kivy.metrics import Metrics

#SFX_FLAP = SoundLoader.load("audio/flap.wav")
#Multi Load Flapping sound effect

#class MultiSound(object):
    #def __init__(self, file, num):
    #    self.num = num
    #    self.sounds = [SoundLoader.load(file) for n in range(num)]
    #    self.index = 0

    #def play(self):
    #    self.sounds[self.index].play()
    #    self.index += 1
    #    if self.index == self.num:
    #        self.index = 0

#SFX_FLAP = MultiSound("audio/flap.wav", 3)
#SFX_SCORE = SoundLoader.load("audio/score.wav")
#SFX_DIE = SoundLoader.load("audio/die.wav")

BACKGROUND_IMAGE = "images/background.png"
#BIRD_IMAGE = "images/bird.png"
BIRD_WINGUP_IMAGE = "atlas://images/bird_anim/wing-up"
BIRD_WINGMID_IMAGE = "atlas://images/bird_anim/wing-mid"
BIRD_WINGDOWN_IMAGE = "atlas://images/bird_anim/wing-down"
GROUND_IMAGE = "images/ground.png"
TOP_PIPE_IMAGE = "images/pipe_top.png"
BOTTOM_PIPE_IMAGE = "images/pipe_bottom.png"

#atlas file: bird_anim.atlas, JSON file containing the pixel positions of the frames in the image:
#{
# "bird_anime.png": {
    #"wing-up": [1, 1, 34, 24],
    #"wing-mid": [37, 1, 34, 24],
    #"wing-down": [73, 1, 34, 24]
    #}
#}

#Game Classes
class Sprite(Image):
    def __init__(self, **kwargs):
        #super(Sprite, self).__init__(**kwargs) # For testing
        #self.size = self.texture_size # For testing
        super(Sprite, self).__init__(allow_stretch=True, **kwargs)
        self.texture.mag_filter = 'nearest'
        w, h = self.texture_size
        self.size = (params.scale * w, params.scale * h)

class Bird(Sprite):
    def __init__(self, pos):
        super(Bird, self).__init__(source=BIRD_WINGUP_IMAGE, pos=pos)
        self.velocity_y = 0
        self.gravity = -.3 * params.scale

    def update(self):
        self.velocity_y += self.gravity
        self.velocity_y = max(self.velocity_y, -10 * params.scale)
        self.y += self.velocity_y
        if self.velocity_y < -5 * params.scale:
            self.source = BIRD_WINGUP_IMAGE
        elif self.velocity_y < 0:
            self.source = BIRD_WINGMID_IMAGE

    def on_touch_down(self, *ignore):
        self.velocity_y = 4.5 * params.scale
        self.source = BIRD_WINGDOWN_IMAGE
        #SFX_FLAP.play()

class Background(Widget):
    def __init__(self, source):
        super(Background, self).__init__()
        self.image = Sprite(source=source)
        self.add_widget(self.image)
        self.size = self.image.size
        self.image_dupe = Sprite(source=source, x=self.width)
        self.add_widget(self.image_dupe)

    def update(self):
        self.image.x -= 2 * params.scale
        self.image_dupe.x -= 2 * params.scale

        if self.image.right <= 0:
            self.image.x = 0
            self.image_dupe.x = self.width

class Ground(Sprite):
    def update(self):
        self.x -= 2  * params.scale
        if self.x < -24  * params.scale: #Note: Ground repeats at 24px
            self.x += 24  * params.scale

class Pipe(Widget):
    def __init__(self, pos):
        super(Pipe, self).__init__(pos=pos)
        self.top_image = Sprite(source=TOP_PIPE_IMAGE)
        self.top_image.pos = (self.x, self.y + 3.5*24 * params.scale) #Space Between the Pipes are 3.5 birds apart.
        self.add_widget(self.top_image)
        self.bottom_image = Sprite(source=BOTTOM_PIPE_IMAGE)
        self.bottom_image.pos = (self.x, self.y - self.bottom_image.height)
        self.add_widget(self.bottom_image)
        self.width = self.top_image.width
        self.scored = False

    def update(self):
        self.x -= 2
        self.top_image.x = self.bottom_image.x = self.x
        if self.right < 0:
            self.parent.remove_widget(self)

class Pipe_set(Widget):
    add_pipe = 0
    def update(self, dt):
        for child in list(self.children):
            child.update()
        self.add_pipe -= dt
        if self.add_pipe < 0:
            #y = random.randint(self.y + 50, self.height - 50 - 3.5*24)
            y = random.randint(int(self.y + 50 * params.scale),
                 int(self.height - 50 * params.scale - 3.5 * 24 * params.scale))
            self.add_widget(Pipe(pos=(self.width, y)))
            self.add_pipe = 4.5

class Blank(Widget):
    def __init__(self, pos, size):
        super(Blank, self).__init__()
        with self.canvas:
            Color(0, 0, 0)
            Rectangle(pos=pos, size=size)
            Color(1, 1, 1)

class Game(Widget):
    def __init__(self):
        super(Game, self).__init__()
        self.background = Background(source=BACKGROUND_IMAGE)
        self.size = self.background.size
        self.add_widget(self.background)
        self.ground = Ground(source=GROUND_IMAGE)
        self.pipe_set = Pipe_set(pos=(0, self.ground.height), size=self.size)
        self.add_widget(self.pipe_set)
        self.add_widget(self.ground)
        self.score_label = Label(center_x=self.center_x,
                                 top=self.top - 30 * params.scale, text="0")
        self.add_widget(self.score_label)
        self.bird = Bird(pos=(20 * params.scale, self.height / 2))
        self.add_widget(self.bird)
        self.over_label = Label(center=self.center, opacity=0,
                                text = "Game Over")
        self.add_widget(self.over_label)
        self.add_widget(Blank(*params.blank_rect))
        Clock.schedule_interval(self.update, 3.5/60.0)
        self.game_over = False
        self.score = 0

    def update(self, dt):
        if self.game_over:
            return
        #print("delta time")
        self.background.update()
        self.bird.update()
        self.ground.update()
        self.pipe_set.update(dt)

        if self.bird.collide_widget(self.ground):
            self.game_over = True
        for pipe in self.pipe_set.children:
            if pipe.top_image.collide_widget(self.bird):
                self.game_over = True
            elif pipe.bottom_image.collide_widget(self.bird):
                self.game_over = True
            elif not pipe.scored and pipe.right < self.bird.x:
                pipe.scored = True
                self.score += 1
                self.score_label.text = str(self.score)
                #SFX_SCORE.play()
            elif pipe.top_image.collide_widget(self.bird):
                self.game_over = True

        if self.game_over:
            #print("Game Over! Score:", self.score) for testing
            #SFX_DIE.play()
            self.over_label.opacity = 1
            self.bind(on_touch_down = self._on_touch_down) #Not active while the game is being played

    def _on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(Menu())

class Menu(Widget):
    def __init__(self):
        super(Menu, self).__init__()
        self.add_widget(Sprite(source=BACKGROUND_IMAGE))
        self.size = self.children[0].size
        self.add_widget(Ground(source=GROUND_IMAGE))
        self.add_widget(Label(center=self.center, text="Tap to Start"))
        self.add_widget(Blank(*params.blank_rect))

    def on_touch_down(self, *ignore):
        parent = self.parent
        parent.remove_widget(self)
        parent.add_widget(Game())

class GameApp(App):
    def build(self):
        #game = Game() #For Testin
        #Window.size = game.size #For Testing


        Window.size = (288, 384) #For Testing

        params.init()
        top = Widget()
        top.add_widget(Menu())
        #return game #For Testing
        return top

class params(object):
    def init(self):
        self.bg_width, self.bg_height = 288, 384
        self.width, self.height = Window.size
        self.center = Window.center
        ws = float(self.width) / self.bg_width
        hs = float(self.height) / self.bg_height
        self.scale = min(ws, hs)
        Logger.info('size=%r; dpi=%r; density=%r; SCALE=%r',
            Window.size, Metrics.dpi, Metrics.density, self.scale)
        if ws > hs:
            gap = self.width - (self.bg_width * hs)
            self.blank_rect = ((self.width - gap, 0), (gap, self.height))
        else:
            gap = self.height - (self.bg_height * ws)
            self.blank_rect = ((0, self.height - gap), (self.width, gap))
params = params()

if __name__ == "__main__":
    GameApp().run()
