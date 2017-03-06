# Super Mario Knockoff
# by Stefan Compton
# Let's-a-go!

# Do some imports
import simplegui, math, random

'''
to do list
1. fix shrink and grow / add powerups
2. add more enemies           
3. add MORE levels       
'''

# a Game class to keep all the variables associated with the game environment and setup - few globals

class Game:
    # set up some variables
    # width and height of screen
    width = 600
    height = 600
    # center of the screen
    centerx = width / 2
    centery = height / 2
    # the position of the camera (left of screen)
    # when camx == 0, the left side of screen is at x = 0 
    camx = 0
    # the acceleration rate at which things fall
    gravity = 0.45
    # images for the ground
    earth = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/stone.png')
    grass = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/stgrass.png')
    grassl = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/stgrassl.png')
    grassr = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/stgrassr.png')
    grasslr = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/stgrasslr.png')
    # a list of images for ? blocks - by using a list i can change index to change the image
    blocks = [simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/question.png'), simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/block2.png')]
    # a background graphic - it turned out to be too busy so it's covered by a semi-transparent rectangle 
    backdrop = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/backdrop.png')
    # our titular hero - 8 frames of animation
    mario = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/Mario-41x21x8.png')
    # the background is made up of a list of lists representing x and y coords
    # so the block at x = 2, y = 1 is [2][1]
    # each block is just a number representing the index of this list of images
    images = [earth, grass, grassl, grassr, grasslr]
    # some logos for the intro screen
    logo1 = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/super-mario-logo.png')
    logo2 = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/logo_2.png')
    # the ghost that makes an appearance on the outro
    boo = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/boo.png')
    # mushroom enemy
    mushroom = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/mushroom.png')
    # Mushroom powerup
    powerMushroom = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/mushroom2.png')
    # this is for when there are multiple enemy types - i can reuse code better by indexing a list based on type
    enemies = [mushroom]
    # this finishing gate at the end of the level - it's in two pieces so i can move the bar up and down as in super mario world (my inspiration for this project!)
    finishGate = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/finishgate.png')
    finishLine = simplegui.load_image('https://dl.dropboxusercontent.com/u/58318455/Mario/finishline.png')
    # This is a list of all images used to check if the are loaded yet - have to remember to add any new images here
    all_images = [earth, grass, grassl, grassr, grasslr, backdrop, mario, logo1, logo2, finishGate, finishLine, boo, powerMushroom] + enemies + blocks
    # the source size of the basic tile used for my tiled background
    tileSize = [20, 20]
    # the size of the source mario graphic
    playerSize = [21, 41]
    # tiles with no block in are air - i'm using this as the type is not "int" 
    airImg = [-1, -1]
    # indexes for the terrain types
    earthImg, grassImg, grassImgL, grassImgR, grassImgLR = 0, 1, 2, 3, 4
    # to give the game that old-skool pixelated look everything is scaled up by the scale when it is drawn
    scale = 2
    # sound effects and music - it should be clear what's what
    letsgo_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/sm64_mario_lets_go.wav')
    oneup_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_1-up.wav')
    breakblock_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_break_block.wav')
    coin_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_coin.wav')
    dragoncoin_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_dragon_coin.wav')
    jump_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_jump.wav')
    loselife_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_lost_a_life.wav')
    mushroom_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_power-up_appears.wav')
    powerup_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_power-up.mp3')
    powerdown_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/power_down.mp3')
    iris_sound = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/smw_goal_iris-out.mp3')
    level_clear_music = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/levelclear.mp3')
    title_music = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/intro.mp3')
    # when i implement firther levels this list will be used to determine the correct music to play
    level_music = [simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/level1.mp3')]
    ghost_music = simplegui.load_sound('https://dl.dropboxusercontent.com/u/58318455/Mario/ghostlevel.mp3')
    # this is going to be filled with nmbers representing the height of the terrain, and generated by levelgen helper function
    levels = []
    # this is used to index into the lists 'levels' and 'level_music' and is passed to the background constructor
    level = 0 
    lives = 3
            
# Helper functions
# 
# level generator helper function

def levelGen(step, cont, gaps, limit = 5):
    '''
    Generate a string of numbers, one for each column of blocks to represent the height of the terrain
    This is going to be interpreted by the background class to generate a background. 
    Start with a random seed 2-5 and then add between +2 and -2 up to a limit of 'limit'
    '''
    length = 10 * Game.width / (Game.scale * Game.tileSize[0] * cont) # length of array of height values, divided by contiguous blocks of same height
    current = random.randint(2, limit - 2)
    result = []
    for blocks in range(length):
        for block in range(cont):
            result.append(current)
        if blocks < length - 2:
            current += (random.randrange(-step, step))
        if current < 2:
            current = 2
        elif current > limit:
            current = limit
       
    # insert some gaps to jump over at even spaces        
    for num in range(10, length * cont - 6, length * cont / gaps):
        for xval in range(num - 2, num + 2):
            result[xval] = 0
    return result

for x in range(10):
    Game.levels.append(levelGen(2, 10 - x / 2, 5))

# Need classes for the Player, the Background and Enemies
# Let's start with background and blocks

class Block:
    '''
    Blocks are the blocks mario can hit with his head
    initially they all look the same and either dispense a coin
    or a mushroom
    '''
    def __init__(self, x, y, size, btype = 0):
        # btype is used to index into a list of images - they will be in pairs - 0 and 1, 2 and 3 and so on
        self.btype = btype
        self.x = x
        self.y = y
        self.size = size
        self.active = True
        self.frame = 0
        # is the block a coin block?
        self.cblock = True

    def getHeight(self):
        '''
        getHeight and getwidth enable code reuse and also simplify code for debugging
        '''
        return self.size[1] * Game.scale

    def getWidth(self):
        return self.size[0] * Game.scale


    def update(self):
        '''
        this is the update code or the block
        this is where we will put animation code
        '''
        # check if mario hits the block with his head
        # first check mario is alive
        if GameLogic.player.isAlive:
            # now set up coordinate values for mario and the block - this makes debugging much easier!
            m_top_right_x = GameLogic.player.x + GameLogic.player.getWidth() / 2
            m_top_x = GameLogic.player.x
            m_top_left_x = GameLogic.player.x - GameLogic.player.getWidth() / 2
            m_top_y = GameLogic.player.y - GameLogic.player.getHeight() / 2
            block_l_x = self.x
            block_r_x = self.x + self.getWidth()
            block_t_y = self.y + self.getHeight() / 2
            block_b_y = self.y + self.getHeight()
            # now check if mario top left or mario top center or mario top right hit the lower part of the block
            if (m_top_left_x > block_l_x and m_top_left_x < block_r_x and m_top_y > block_t_y and m_top_y < block_b_y) or (m_top_x > block_l_x and m_top_x < block_r_x and m_top_y > block_t_y and m_top_y < block_b_y) or (m_top_right_x > block_l_x and m_top_right_x < block_r_x and m_top_y > block_t_y and m_top_y < block_b_y):
                # if so make him stop jumping and rebound down 
                GameLogic.player.isJumping = False
                GameLogic.player.vel[1] = 2
                GameLogic.player.isFalling = True
                # if the mario is directly underneath the block 
                if m_top_x > block_l_x and m_top_x < block_r_x:
                    # if it is inactive and there are no ongoing animations 
                    if self.frame == 40:
                        # reset the animation - this is so that non-active blocks wobble when you hit them
                        self.frame = 0 
                    # if the block is active - ie not yet touched by head of plumber
                    elif self.active:
                        # play sound, increase score, change graphic and make block dead - maybe give a mushroom :-)
                        if random.randint(1,6) == 6:
                            GameLogic.mushroomSet.add(Mushroom(self.x + self.getWidth() / 2, self.y + self.getHeight() / 4, True))
                            self.cblock = False
                            self.active = False
                        else:
                            Game.coin_sound.play()
                            GameLogic.score += 50 
                            GameLogic.animationSet.add(Animation(self.x, self.y, 50))
                            self.active = False
 
    def draw(self, canvas):
        '''
        each block contains a frame counter, and once they are hit it will start advancing
        animation runs from frame 0 - 30 in 3s and then advances to 40 to indicate that animation is done
        '''
        # if the block has been hit, but is not yet finished animation
        if self.active == False and self.frame < 40:
            # if the main part of the animation is still running
            if self.frame < 30:
                # advance frame
                self.frame += 3
                # if the block being drawn is an active block (note this is different to self.active, which changes as soon as the block is hit) 
                # the block is a coin block
                if self.btype % 2 == 0 and self.cblock:
                    # draw a gold and yellow 'coin' travelling upwards 
                    canvas.draw_circle([self.x + self.getWidth() / 2 - Game.camx, self.y - self.frame], 7, 1, 'Gold', 'Gold')
                    canvas.draw_circle([self.x + self.getWidth() / 2 - Game.camx, self.y - self.frame], 3, 1, 'Yellow', 'Yellow')

            else:
                # turn an active block (even number) will turn into an inactive block (odd number) but not the other way around
                self.btype += (self.btype + 1) % 2  
                # the main animation is done so advance to frame 40
                self.frame = 40  
        # move the block up and down in a sine wave when headbutted
        movement = (8 * math.sin(self.frame / 10.0)) if self.frame <= 30 else 0 # move the block when headbutted
        # draw the block - note btype is used to index into a list of block images, and thus xhange the image
        canvas.draw_image(Game.blocks[self.btype], [self.size[0] / 2, self.size[1] / 2], self.size, [self.x - Game.camx + self.size[0] * Game.scale / 2, self.y + self.size[1] * Game.scale / 2 - movement], [self.size[0] * Game.scale, self.size[1] * Game.scale]) 
        

class Background:
    def __init__(self, level):
        '''
        create a background - a list of lists 'tiles'
        tiles[x][y] is the tile at x and y coordinates
        with the type of material present
        represented by the index in the list 'images'
        '''
        # size and center of finish gates and the 'line' between them
        self.finishCenter = [24, 72] 
        self.finishSize = [48, 145] 
        self.finishLineCenter = [12, 4]
        self.finishLineSize = [24, 8]
        # frame is always used for aimation - it gets updated once per draw cycle by .update() 
        self.frame = 0
        self.width = 10 * Game.width / (Game.scale * Game.tileSize[0]) # the background is 10 times the screen width (and everything is scaled)
        self.height = Game.height / (Game.scale * Game.tileSize[1]) # and the height of the screen
        self.tiles = []
        # generate 
        for x in range(self.width):
            self.tiles.append([])
            for y in range(self.height):
                if self.height - y > Game.levels[level][x]:
                    if self.height - y - 3 == Game.levels[level][x] and (x % 10 == 2 or x % 10 == 3) and Game.levels[level][x] != 0:
                        self.tiles[x].append(Block(x * Game.tileSize[0] * Game.scale, y * Game.tileSize[1] * Game.scale, Game.tileSize))
                    else:
                        self.tiles[x].append(Game.airImg)
                elif self.height - y == Game.levels[level][x]: # really complicated nested if statements to determine
                    if x == 0:                                  # whether the grass should go on left or right (and make sure we're always indexing in-bounds)
                        if Game.levels[level][x] > Game.levels[level][x + 1]:
                            self.tiles[x].append(Game.grassImgR)
                        else:
                            self.tiles[x].append(Game.grassImg)
                    elif x == self.width - 1:
                        if Game.levels[level][x] > Game.levels[level][x - 1]:
                            self.tiles[x].append(Game.grassImgL)
                        else:
                            self.tiles[x].append(Game.grassImg)
                    elif Game.levels[level][x] > Game.levels[level][x - 1] and Game.levels[level][x] > Game.levels[level][x + 1]:
                        self.tiles[x].append(Game.grassImgLR)
                    elif Game.levels[level][x] > Game.levels[level][x + 1]:
                        self.tiles[x].append(Game.grassImgR)
                    elif Game.levels[level][x] > Game.levels[level][x - 1]:
                        self.tiles[x].append(Game.grassImgL)
                    else:
                        self.tiles[x].append(Game.grassImg)
                else:
                    self.tiles[x].append(Game.earthImg)

    def update():
        pass
        
    def draw(self, canvas):
        '''
        the background has to draw itself
        based on the player X position
        '''
        self.frame += 1
        # draw our backdrop which scrolls at a slower speed - NB it's too busy so i've covered it with a semi-transparent rectangle the size of the screen 
        canvas.draw_image(Game.backdrop, [480 + 960 * Game.camx / (9 * Game.width), 700], [960, 1000], [Game.centerx, Game.centery], [Game.width, Game.height])
        GameLogic.draw_rect(canvas, [0, 0], [Game.width, Game.height], 'rgba(175, 255, 255, 0.8)')

        for mushroom in GameLogic.mushroomSet:
            mushroom.update()
            # draw emerging mushrooms here behind the block
            if mushroom.emerging:
                mushroom.draw(canvas)
        for x in range(Game.camx / (Game.tileSize[0] * Game.scale), 2 + (Game.camx + Game.width) / (Game.tileSize[0] * Game.scale)):
            for y in range(len(self.tiles[x])):
                if self.tiles[x][y] != Game.airImg:
                    if type(self.tiles[x][y]) == int:
                        canvas.draw_image(Game.images[self.tiles[x][y]], [Game.tileSize[0] / 2, Game.tileSize[1] / 2], 
                                      Game.tileSize, [Game.tileSize[0] * Game.scale * ((x * 2 + 1) / 2) - Game.camx + Game.tileSize[0] * Game.scale / 2, Game.tileSize[1] * Game.scale * ((y * 2 + 1) / 2) + Game.tileSize[0] * Game.scale / 2], 
                                      [Game.tileSize[0] * Game.scale, Game.tileSize[1] * Game.scale])
                    else:
                        self.tiles[x][y].update()
                        self.tiles[x][y].draw(canvas)
        for mushroom in GameLogic.mushroomSet:
            # draw non-emerging mushrooms here in front of the rest of the background
            if mushroom.emerging == False:
                mushroom.draw(canvas)
        # if we're near the end, draw the finish line
        if Game.camx > 8 * Game.width:
            canvas.draw_image(Game.finishGate, self.finishCenter, self.finishSize, [138 * Game.scale * Game.tileSize[0] - Game.camx, Game.height - Game.scale * Game.tileSize[0] * Game.levels[Game.level][138] - Game.scale * self.finishSize[1] / 2], 
                              [self.finishSize[0] * Game.scale, self.finishSize[1] * Game.scale])
            if GameLogic.player.x < 138 * Game.scale * Game.tileSize[0]:
                canvas.draw_image(Game.finishLine, self.finishLineCenter, self.finishLineSize, [138 * Game.scale * Game.tileSize[0] - 8 - Game.camx, math.sin(self.frame / 40.0) * 100 + Game.height - Game.scale * Game.tileSize[0] * Game.levels[Game.level][138] - Game.scale * self.finishSize[1] / 2], 
                                  [self.finishLineSize[0] * Game.scale, self.finishLineSize[1] * Game.scale])

    def getTile(self, pos1, pos2):
        '''
        Is the specified line on a tile?        
        '''
        for x in range(pos1[0] / (Game.tileSize[0] * Game.scale), 1 + pos2[0] / (Game.tileSize[0] * Game.scale)):
            if x >= 0 and x < len(self.tiles):
                for y in range(int(pos1[1] / (Game.tileSize[1] * Game.scale)), int(1 + pos2[1] / (Game.tileSize[1] * Game.scale))):
                    if y >= 0 and y < len(self.tiles[0]):
                        if self.tiles[x][y] != [-1, -1]:
                            return True

        return False

# new class for mushrooms .. yummy :-)

class Mushroom:
    def __init__(self, x, y, isEmergingFromBlock):
        self.speed = 2
        self.size = [16, 16]
        self.x = x
        self.y = y
        self.emerging = isEmergingFromBlock
        self.ticker = 0
        self.vel = [0, 0]
        self.acc = [0, 0]
        Game.mushroom_sound.play()

    def update(self):
        #if GameLogic.player.collision(set(self)) > -1:
        #    print 'mushroom collider!'
        
        self.ticker += 1
        if self.ticker > 30:
            self.emerging = False
        elif self.ticker == 30:
            self.vel[0] = self.speed if random.randint(1,2) == 1 else -self.speed
            self.vel[1] = -self.speed
        if self.emerging:
            self.y -= 1
        else:
            # stop falling through blocks
            if GameLogic.backgnd.getTile([self.x - self.getWidth() / 2 + 2, self.y + self.getHeight() / 2 + 2], [self.x + self.getWidth() / 2 - 2, 
                                                                                         self.y + self.getHeight() / 2 + 2]):
                self.isFalling = False
                self.vel[1] = 0.0
            else:
                self.isFalling = True

            # turn around when hitting a block
            if self.vel[0] > 0 and GameLogic.backgnd.getTile([self.x + self.getWidth() / 4 + 2, 
                                   self.y - self.getHeight() / 4 + 2], [self.x + self.getWidth() / 4 + 2, self.y + self.getHeight() / 4 - 4]) or self.vel[0] < 0 and GameLogic.backgnd.getTile([self.x - self.getWidth() / 4 - 2, 
                                   self.y - self.getHeight() / 4 + 2], [self.x - self.getWidth() / 4 - 2, self.y + self.getHeight() / 4 - 4]):
                self.vel[0] *= -1

            if self.isFalling:
                self.acc[1] = Game.gravity
            self.vel[1] += self.acc[1]
            self.x += int(self.vel[0])
            self.y += int(self.vel[1])
    
    def getHeight(self):
        return self.size[1] * Game.scale
    
    def getWidth(self):
        return self.size[0] * Game.scale  

    def draw(self, canvas):
        #GameLogic.draw_rect(canvas, [self.x - Game.camx - 10, self.y-10], [self.x - Game.camx + 10, self.y+10], 'Black')
        canvas.draw_image(Game.powerMushroom, [self.size[0] / 2, self.size[1] / 2], self.size, [self.x - Game.camx, self.y], [self.getWidth(), self.getHeight()])




class Player:
    def __init__(self):
        self.x = self.getWidth() * 2
        self.y = Game.height / 6
        self.isJumping = False
        self.isFalling = False
        self.isShrinking = False
        self.isGrowing = False
        self.size = 0.75
        self.acc = [0.0, 0.0]
        self.vel = [0.0, 0.0]
        self.image = 0
        self.frame = 0
        self.isRight = True
        self.lives = 0
        self.isAlive = True
        self.runSpeed = 1
        self.topMushroom = False

    def getWidth(self):
        return Game.playerSize[0] * Game.scale

    def getHeight(self):
        return Game.playerSize[1] * self.size

    def update(self):
        if self.isAlive:
            if self.x >= 138 * Game.scale * Game.tileSize[0]:
                GameLogic.levelClear = True
                GameLogic.state = 'intro'
                Game.level_music[Game.level].pause()
                Game.level_music[Game.level].rewind()
                Game.level_clear_music.play()
                self.isAlive = False
                self.frame = 0
                self.acc[0] = 0
            if GameLogic.spawning == True:  ## start of life/level where mario walks onto screen
                if self.frame == 0:
                    while (not GameLogic.isSafe()):
                        Game.camx -= Game.tileSize[0] * Game.scale / 2  ## when spawning, if the background has a gap or is uneven
                                                                        ## move camera left half a block
                self.x = Game.camx + self.frame
                self.y = Game.height - self.getHeight() / 2 - (Game.levels[Game.level][Game.camx / (Game.tileSize[0] * Game.scale)] * Game.scale * Game.tileSize[1])
                self.image = (self.frame / 8) % 2
                if self.frame > 30:
                    Game.level_music[Game.level].play()
                
                if self.frame > 120:
                    GameLogic.spawning = False
                    self.isFalling = False    
                    self.acc = [0.0, 0.0]
                    self.vel = [0.0, 0.0]
                    self.image = 0
                    self.frame = 0
                    self.isRight = True
                self.frame += 1
            else:
                # Stop falling through the floor
                if GameLogic.backgnd.getTile([self.x - self.getWidth() / 2 + 4, self.y + self.getHeight() / 2 + 2], [self.x + self.getWidth() / 2 - 4, 
                                                                                             self.y + self.getHeight() / 2 + 2]) and self.isJumping == False:
                    self.isFalling = False
                    self.vel[1] = 0.0
                else:
                    self.isFalling = True
                # stop running through blocks
                if self.vel[0] > 0 and GameLogic.backgnd.getTile([self.x + self.getWidth() / 2 + 2, 
                                       self.y - self.getHeight() / 2 + 2], [self.x + self.getWidth() / 2 + 2, self.y + self.getHeight() / 2 - 4]) or self.vel[0] < 0 and GameLogic.backgnd.getTile([self.x - self.getWidth() / 2 - 2, 
                                       self.y - self.getHeight() / 2 + 2], [self.x - self.getWidth() / 2 - 2, self.y + self.getHeight() / 2 - 4]):
                    self.vel[0] = 0
                if self.isFalling:
                    self.acc[1] = Game.gravity
                if self.isJumping:
                    if self.vel[1] > 2:
                        self.isJumping = False
                self.vel[0] += self.acc[0]
                self.vel[1] += self.acc[1]
                self.vel[0] *= 0.93
                self.vel[1] *= 0.93
                self.x += int(self.vel[0])
                self.y += int(self.vel[1])
                if self.x - Game.camx < Game.playerSize[0] / 2:
                    self.x = Game.camx + Game.playerSize[0] / 2
                if self.x > 10 * Game.width - Game.playerSize[0] / 2:
                    self.x = 10 * Game.width - Game.playerSize[0] / 2
                self.frame += 1
                self.frame %= 12
                frameno = 0 if self.isRight else 3
                if self.isJumping:
                    self.image = 2 if self.isRight else 5 # jumping
                elif self.acc[0] > 0.1:
                    self.image = frameno + self.frame / 4 # moving right
                elif self.acc[0] < -0.1:
                    self.image = frameno + self.frame / 4 # moving left
                else:
                    self.image = 0 if self.isRight else 3 # stopped
                if self.x > Game.camx + Game.width / 2:
                    Game.camx += (self.x - (Game.camx + Game.centerx)) / 20 # make the camera run faster as we go more right
                #elif self.x < Game.camx + Game.centerx - 170:
                    #Game.camx -= ((Game.camx + Game.centerx) - self.x) / 50 # make the camera run faster as we go more left
                if Game.camx < 0:
                    Game.camx = 0
                if Game.camx >= 9 * Game.width - 10:
                    Game.camx = 9 * Game.width - 10
                if self.y + self.getHeight() / 2 > Game.height - 4:
                    self.isAlive = False
                    self.lives -= 1
                    self.frame = -10
                    GameLogic.enemySet = set()
                collide = self.collision(GameLogic.enemySet)
                if collide == 0:  # jumped on the enemy
                    GameLogic.score += 50
                    GameLogic.animationSet.add(Animation(self.x - self.getWidth() / 2, self.y - self.getHeight() / 2, 50))
                    self.isJumping = True
                    self.vel[1] = -15
                    Game.jump_sound.play()
                elif collide >= 1:
                    # dead
                    if self.size < 1:
                        self.isAlive = False
                        self.lives -= 1
                        self.frame = -10
                        GameLogic.enemySet = set()
                    else:
                        self.shrink()
        else:
            if GameLogic.levelClear == False:
                Game.level_music[Game.level].pause()
                Game.level_music[Game.level].rewind()
                Game.loselife_sound.play()
                self.size = 0.75
                GameLogic.spawning = True ## stop controls and music playing 
                # wait 10 frames before starting 
                self.image = 6
                if self.frame < 0:
                    self.poi = self.y # set the point of incident = mario's y pos when he died
                elif self.frame < 45:
                    # animate dead mario
                    self.image = 6 + self.frame % 2
                    # move in a sin wave up and then down
                    temp = 100 if self.frame < 30 else 300
                    self.y = int(self.poi - self.getHeight() / 2 - temp * math.sin(self.frame * 2 * math.pi / 60))
                elif self.frame < 180:
                    pass
                else:
                    if self.lives <= 0:
                        GameLogic.gameover()
                    else:
                        self.isAlive = True
                        self.frame = -1
                self.frame += 1
            else:
                self.frame += 1
                if Game.camx < 9 * Game.width - Game.scale * Game.tileSize[0] - 1:
                    Game.camx += 1
                if self.frame >= 420:
                    self.goRight()
                    self.image = (self.frame % 12) / 4

                    '''
                    if Game.camx < 9 * Game.width - 20:
                        Game.camx += 1
                    '''
                else:
                    if GameLogic.backgnd.getTile([self.x - self.getWidth() / 2 + 4, self.y + self.getHeight() / 2 + 2], [self.x + self.getWidth() / 2 - 4, 
                                                                                                 self.y + self.getHeight() / 2 + 2]):
                        self.isFalling = False
                        self.vel[1] = 0
                    else:
                        self.isFalling = True
                    if self.isFalling:
                        self.acc[1] = Game.gravity
                    else:
                        self.acc[1] =  0
                    if self.x > Game.camx + Game.centerx + 100:
                        Game.camx += (self.x - (Game.camx + Game.centerx)) / 50 # move camera
                    if Game.camx >= 9 * Game.width - 10:
                        Game.camx = 9 * Game.width - 10
                self.vel[0] += self.acc[0]
                self.vel[1] += self.acc[1]
                self.vel[0] *= 0.93
                self.vel[1] *= 0.93
                self.x += int(self.vel[0])
                self.y += int(self.vel[1])

                if self.frame > 480:
                    GameLogic.tick = 0
                    frame.set_draw_handler(GameLogic.outro)

    def collision(self, objset):
        '''
        test for collision with a set
        return 0 if the collision is on the bottom - jumped on
        return 1 if on the left or right - dead if it's an enemy, do nothing for a block
        return 2 for headbutt - get coin out of block, die if its an enemy
        '''
        for obj in objset:
            if abs (obj.y - obj.getHeight() / 4 - (self.y + self.getHeight() / 2)) < obj.getHeight() / 2 and abs(self.x - obj.x) < self.getWidth() / 2 + obj.getWidth() / 2:  # foot collision
                objset.remove(obj)
                return 0
            elif abs(self.x - obj.x) < self.getWidth() / 2 + obj.getWidth() / 2 and abs(self.y - obj.y) < self.getHeight() / 2 + obj.getHeight() / 2: # general collision
                objset.remove(obj)
                return 1
        return -1 # no collision
             


          
    def goRight(self):
        self.acc[0] = 0.5 * self.runSpeed
        self.isRight = True
       
    def goLeft(self):
        self.acc[0] = -0.5 * self.runSpeed
        self.isRight = False
        
    def walk(self):
        self.runSpeed = 0.4

    def run(self):
        self.runSpeed = 1.0

    def stop(self):
        self.acc[0] = 0.0
        

    def jump(self):
        if GameLogic.backgnd.getTile([self.x - self.getWidth() / 2 + 2, self.y + self.getHeight() / 2 + 2], [self.x + self.getWidth() / 2 - 2, 
                                                                                     self.y + self.getHeight() / 2 + 2]):
            self.isJumping = True
            self.vel[1] = -20
            Game.jump_sound.play()

    def grow(self):
        if self.size == 0.75:
            self.size = 1
            Game.powerup_sound.play()
            self.y -= self.getHeight() / 6
            self.isGrowing = True
            GameLogic.tick2 = 0

    def shrink(self):
        if self.size == 1:
            self.size = 0.75
            Game.powerdown_sound.play()
            self.y += self.getHeight() / 8
            self.isShrinking = True
            GameLogic.tick2 = 0
            if self.topMushroom:
                GameLogic.mushroomSet.add(Mushroom(Game.camx + Game.centerx, Game.height / 10, False))
                self.topMushroom = False

    def draw(self, canvas):
        '''
        draw player image at x, y offset by the camera
        '''
        canvas.draw_image(Game.mario, [self.image * Game.playerSize[0] + Game.playerSize[0] / 2, Game.playerSize[1] / 2], Game.playerSize, [self.x - Game.camx, self.y], 
                          [Game.playerSize[0] * Game.scale, Game.playerSize[1] * self.size])
        # draw a spare mushroom if mario has one
        if self.topMushroom:
            canvas.draw_image(Game.powerMushroom, [8, 8], [16, 16], [Game.centerx, Game.height / 10], [48, 48])
        

class Enemy:
    sizes = [[19, 15]] # when adding an enemy type put it's size here
    def __init__(self, x, y, entype, speed = 1): 
        self.x = x
        self.y = y
        self.entype = entype # 0 = mushroom, 
        self.isFalling = False
        self.speed = speed
        if GameLogic.player.x > self.x:
            self.vel = [self.speed, 0]
        else:
            self.vel = [-self.speed, 0]
        self.acc = [0, 0]
        self.size = Enemy.sizes[self.entype] 

    def draw(self, canvas):
        if self.vel[0] > 0:  
            self.frame = GameLogic.tick % 30 / 15 # going right - frame 0 & 1
        else:
            self.frame = 2 + GameLogic.tick % 30 / 15 # going left - frame 2 & 3
        
        canvas.draw_image(Game.enemies[self.entype], [self.frame * self.size[0] + self.size[0] / 2, self.size[1] / 2], self.size, [self.x - Game.camx, self.y], 
                          [self.size[0] * Game.scale, self.size[1] * Game.scale])
        
        #todo

    def update(self):
        # stop falling through blocks
        if GameLogic.backgnd.getTile([self.x - Game.tileSize[0] / 2 + 2, self.y + Game.tileSize[1] / 2 + 2], [self.x + Game.tileSize[0] / 2 - 2, 
                                                                                     self.y + Game.tileSize[1] / 2 + 2]):
            self.isFalling = False
            self.vel[1] = 0.0
        else:
            self.isFalling = True

        # turn around when hitting a block
        if self.vel[0] > 0 and GameLogic.backgnd.getTile([self.x + Game.tileSize[0] / 2 + 2, 
                               self.y - Game.tileSize[1] / 2 + 2], [self.x + Game.tileSize[0] / 2 + 2, self.y + Game.tileSize[1] / 2 - 4]) or self.vel[0] < 0 and GameLogic.backgnd.getTile([self.x - Game.tileSize[0] / 2 - 2, 
                               self.y - Game.tileSize[1] / 2 + 2], [self.x - Game.tileSize[0] / 2 - 2, self.y + Game.tileSize[1] / 2 - 4]):
            self.vel[0] *= -1

        if self.isFalling:
            self.acc[1] = Game.gravity
        self.vel[1] += self.acc[1]
        self.x += int(self.vel[0])
        self.y += int(self.vel[1])

    def getWidth(self):
        return Game.tileSize[0] * Game.scale

    def getHeight(self):
        return Game.tileSize[1] * Game.scale

class Animation:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        self.amount = str(amount)
        self.frame = 0


    def draw(self, canvas):
        self.frame += 1
        canvas.draw_text(self.amount, [self.x - Game.camx - self.frame / 2, self.y - self.frame / 2], 24 + self.frame, 'rgba(100,0,75,'+str(1.0 / self.frame)+')', 'sans-serif')


# a GameLogic class to keep all the instances, draw handlers and to handle the game logic etc.
class GameLogic:
    tick = 0
    state = "intro"
    backgnd = Background(Game.level)
    player = Player()
    enemySet = set()
    mushroomSet = set()
    animationSet = set()
    player.lives = 3
    score = 0
    spawning = True
    levelClear = True

    def draw_rect(canvas, po1, po2, col):
        canvas.draw_polygon([po1, [po1[0], po2[1]], po2, 
                             [po2[0], po1[1]]], 1, col, col)
    
    def isSafe():
        ''' 
        helper function to test if the ground
        is even and has no gaps
        when spawning Mario
        return true if the first 1/4 of the screen is flat and clear of holes
        '''
        startBlock = Game.camx / (Game.tileSize[0] * Game.scale)
        if startBlock < 1:
            startBlock = 1
        endBlock = startBlock + (Game.width / (3 * Game.tileSize[0] * Game.scale))
        result = True 
        for block in range(startBlock - 1, endBlock + 1):
            if Game.levels[Game.level][block] == 0 or Game.levels[Game.level][block] != Game.levels[Game.level][block + 1]:
                result = False
        return result
    
    #draw handler to load images 
    def loader(canvas):
        result = True
        loaded = 0
        for image in Game.all_images:
            if image.get_width() == 0:
                result = False
            else:
                loaded += 1
        for size in range(75):
            if frame.get_canvas_textwidth('Images Loaded ' +str(loaded) + ' / ' + str(len(Game.all_images)), 100 - size) <= Game.width:
                break
        canvas.draw_text('Images Loaded ' +str(loaded) + ' / ' + str(len(Game.all_images)), [0, Game.centery], 100 - size, 'Black') 
        if result == True:
            Game.coin_sound.play()
            frame.set_canvas_background('Black')
            GameLogic.tick = 0
            frame.set_draw_handler(GameLogic.intro)
        
        for size in range(75):
            if frame.get_canvas_textwidth('< please wait >', 100 - size, 'monospace') <= Game.width / 3:
                break    
        canvas.draw_text('< please wait >', [Game.width / 3, Game.height - 10], 100 - size, 'rgba(0,0,0,'+str(abs(math.sin(GameLogic.tick / 10.0)))+')', "monospace")
        GameLogic.tick += 1

    # Draw handler for 'Intro' mode
    def intro(canvas):
        Game.title_music.play()
        GameLogic.tick += 1
        #GameLogic.draw_sin_squiggle(canvas, Game.logo1, [Game.centerx, Game.height / 3], GameLogic.tick, 20)
        canvas.draw_image(Game.logo1,[261, 108] ,[521, 215], [Game.centerx, Game.height / 3], [Game.width, 3 * Game.height / 4])
        canvas.draw_image(Game.logo2,[142, 43] ,[283, 85], [Game.centerx, 4 * Game.height / 5], [Game.centerx, Game.height / 4])
        numticks = 30
        xmove = Game.centerx / numticks
        ymove = Game.centery / numticks
        p1 = [Game.centerx - xmove * GameLogic.tick, Game.centery - ymove * GameLogic.tick]
        p2 = [Game.centerx + xmove * GameLogic.tick, Game.centery - ymove * GameLogic.tick]
        p3 = [Game.centerx + xmove * GameLogic.tick, Game.centery + ymove * GameLogic.tick]
        p4 = [Game.centerx - xmove * GameLogic.tick, Game.centery + ymove * GameLogic.tick]
        GameLogic.draw_rect(canvas, [0, 0], p2, "white")
        GameLogic.draw_rect(canvas, [Game.width, 0], p3, "white")
        GameLogic.draw_rect(canvas, p4, [Game.width, Game.height], "white")
        GameLogic.draw_rect(canvas, p1, [0, Game.height], "white")
        #if (GameLogic.tick / 30) % 2 == 0:
            
        canvas.draw_text('<press a key>', [Game.width / 3, Game.height - 10], 28, 'rgba(125, 249, 255,'+str(round(abs(math.sin(GameLogic.tick / 20.0)), 2))+')', "monospace")
        
        if GameLogic.tick > 500:
            Game.title_music.pause()
            GameLogic.state = "game"
            frame.set_draw_handler(GameLogic.game)
            Game.letsgo_sound.play()
            frame.set_canvas_background('rgb(135, 206, 250)')
            GameLogic.tick = 0
            GameLogic.spawning = True
            GameLogic.levelClear = False
            
    # Draw handler for 'Game' mode
    def game(canvas):
        # first 
        GameLogic.backgnd.draw(canvas)
        for x in range(GameLogic.player.lives):
            canvas.draw_image(Game.mario, [Game.playerSize[0] / 2, Game.playerSize[1] / 2], Game.playerSize, [20 + 30 * x, 15], [20, 20])
        canvas.draw_text(str(GameLogic.score), [550, 20], 20, 'Black')
        GameLogic.draw_rect(canvas, [Game.centerx - 35, Game.height / 10 - 35], [Game.centerx + 35, Game.height / 10 + 35], 'Yellow')
        GameLogic.draw_rect(canvas, [Game.centerx - 30, Game.height / 10 - 30], [Game.centerx + 30, Game.height / 10 + 30], 'Black')
        if GameLogic.player.isShrinking:
            GameLogic.tick2 += 1
            if (GameLogic.tick2 / 5) % 2 == 0:
                GameLogic.player.size = 0.75 
            else:
               GameLogic.player.size = 1
            if GameLogic.tick2 == 30:
                GameLogic.player.size = 0.75
                GameLogic.player.isShrinking = False
            GameLogic.player.draw(canvas)
            for enemy in GameLogic.enemySet:
                enemy.draw(canvas)
        elif GameLogic.player.isGrowing:
            GameLogic.tick2 += 1
            GameLogic.player.size = 1 if (GameLogic.tick2 / 5) % 2 == 0 else 0.75
            if GameLogic.tick2 == 30:
                GameLogic.player.size = 1
                GameLogic.player.isGrowing = False
            GameLogic.player.draw(canvas)
            for enemy in GameLogic.enemySet:
                enemy.draw(canvas)
        else:
            if GameLogic.spawning == False and GameLogic.levelClear == False: 
                for enemy in GameLogic.enemySet:
                    if enemy.y + Game.scale * Game.tileSize[1] > Game.height - 2:
                        GameLogic.enemySet.remove(enemy)
                    enemy.update()
                    enemy.draw(canvas)
                for mushroom in GameLogic.mushroomSet:
                    if mushroom.y + mushroom.getHeight() / 2 > Game.height - 4 or mushroom.x < mushroom.getWidth() / 2:
                        GameLogic.mushroomSet.remove(mushroom)
                if GameLogic.player.collision(GameLogic.mushroomSet) > -1:
                    if GameLogic.player.size != 1:
                        GameLogic.player.grow()
                    elif GameLogic.player.topMushroom == False:
                         GameLogic.player.topMushroom = True             
                if Game.camx < Game.width * 8.9:
                    if GameLogic.tick % 100 == random.randint(0, 100):  # add an enemy at random intervals as long as we're not at the end of the level
                        GameLogic.enemySet.add(Enemy(GameLogic.player.x + 400, 
                               Game.tileSize[0] * Game.scale * (Game.height / (Game.tileSize[0] * Game.scale) - 1 - Game.levels[Game.level][(GameLogic.player.x + 400)/(Game.tileSize[0]*Game.scale)]), 0, 2))
            GameLogic.player.update()
            GameLogic.player.draw(canvas)
            GameLogic.tick += 1
            for animation in GameLogic.animationSet:
                animation.draw(canvas)
                if animation.frame >= 30:
                    GameLogic.animationSet.remove(animation)
            if GameLogic.levelClear == True and GameLogic.player.frame >= 400:
                x = GameLogic.player.x - Game.camx
                y = GameLogic.player.y
                incFrame = GameLogic.player.frame - 400
                point1 = [x * incFrame / 80, y * incFrame / 80]
                point2 = [Game.width - (Game.width - x) * incFrame / 80, y * incFrame / 80]
                point3 = [x * incFrame / 80, Game.height - (Game.height - y) * incFrame / 80]
                point4 = [Game.width - (Game.width - x) * incFrame / 80, Game.height - (Game.height - y) * incFrame / 80]
                GameLogic.draw_rect(canvas, [0, 0], point3, 'Black')
                GameLogic.draw_rect(canvas, [0, Game.height], point4, 'Black')
                GameLogic.draw_rect(canvas, [Game.width, Game.height], point2, 'Black')
                GameLogic.draw_rect(canvas, [Game.width, 0], point1, 'Black')
                if GameLogic.player.frame == 440:
                    Game.iris_sound.play()


    
    def outro(canvas):
        Game.ghost_music.play()
        GameLogic.tick += 28.0 / 25
        ticker = GameLogic.tick - Game.width
        canvas.draw_text('Thank You For Playing :-) ... more levels, more enemies, powerups, 3D, VR, holographic ... all coming soon ... honest', [0 - ticker, Game.height - 10], 48, 'black')
        if ticker > 2200 and ticker <= 2400:
            canvas.draw_image(Game.boo, [399, 339], [799, 679], [Game.centerx, Game.centery], [Game.width, Game.height])
            t = (2300 - ticker) / 100.0 if ticker <= 2300 else (ticker - 2300) / 100.0 
            GameLogic.draw_rect(canvas, [0,0], [Game.width, Game.height], 'rgba(135, 206, 250,'+str(t)+')')
        if ticker  > 3000:
            Game.title_music.rewind()
            Game.ghost_music.rewind()
            frame.set_draw_handler(GameLogic.loader)
        #canvas.draw_text(str(ticker), [0, 20], 12, 'Black')
        GameLogic.draw_sin_squiggle(canvas, Game.logo1, [Game.centerx, Game.height / 3], GameLogic.tick / 2, 20)

    def draw_sin_squiggle(canvas, image, pos, ticker, div):
        if div == 0:
            div = 1
        for y in range(image.get_height()):
            canvas.draw_image(image, [image.get_width() / 2, y], [image.get_width(), 1], [pos[0] + math.sin((ticker + y) / 20.0) * image.get_width() / div, pos[1] - image.get_height() / 2 + y], [image.get_width(), 1]) 


    def gameover():
        '''
        set conditions to restart the game from the beginning
        '''
        frame.set_draw_handler(GameLogic.loader)
        GameLogic.tick = 0
        GameLogic.tick2 = 0
        GameLogic.state = "intro"
        GameLogic.backgnd = Background(Game.level)
        GameLogic.player = Player()
        GameLogic.enemySet = set()
        GameLogic.player.lives = 3
        GameLogic.score = 0
        GameLogic.spawning = True
        Game.camx = 0
        Game.title_music.rewind()
        GameLogic.player.size = 0.75

def key_down(key):
    if GameLogic.state == 'game' and GameLogic.spawning == False:
        if key == simplegui.KEY_MAP['right']:
            GameLogic.player.goRight()
        elif key == simplegui.KEY_MAP['left']:
            GameLogic.player.goLeft()
        elif key == simplegui.KEY_MAP['space']:
            GameLogic.player.jump()
        elif key == simplegui.KEY_MAP['z']:
            GameLogic.player.walk()

    else:
        GameLogic.tick = 501

def key_up(key):
    if key == simplegui.KEY_MAP['right']:
        GameLogic.player.stop()
    elif key == simplegui.KEY_MAP['left']:
        GameLogic.player.stop() 
    elif key == simplegui.KEY_MAP['z']:
        GameLogic.player.run()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", Game.width, Game.height)
frame.set_canvas_background('White')
frame.set_draw_handler(GameLogic.loader)
frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)

# Start the frame animation
frame.start()
