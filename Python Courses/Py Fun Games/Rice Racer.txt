# "Rice Racer" - A tribute to Sega's 1988 Arcade Game "Power Drift"
#
# I was trying to think of which classic arcade game would be a good match for the tools provided
# by CodeSkulptor and SimpleGUI. SimpleGUI's most exciting graphical feature is the ability to
# scale and rotate images, so I started thinking of the sprite-scalers from the mid-80's, like
# Space Harrier, Out Run and Afterburner. However, the one I remember most vividly is an outrageous
# driving game called Power Drift, which challenged the player to race around tracks that resembled
# roller coasters more than motor racing circuits.
#
# Programming - Steven Knock
# Music       - Andy Denton
# Graphics    - Car, courtesy of Pete Carpenter of http://www.rc-airplane-world.com
#             - Trees, from http://www.immediateentourage.com
#             - Horizon, http://en.wikipedia.org/wiki/File:Spitzkoppe_360_Panorama.jpg
#             - Track, generated using Paint Shop Pro
#
# Current Version (v1.4 - 11th July 2013):
#   in which I updated the code to work with CodeSkulptor's new integer and float rules.
#
# Earlier versions:
# v1.3 - 13th March 2013:
#   in which I added the horizon, music, sound effects, player images, new track, new car images
#   and increased the difficulty.
#
# v1.2: http://www.codeskulptor.org/#user8-gRnuT0e3vD-0.py
#   in which I updated the code to work with the latest version of CodeSkulptor.
#
# v1.1: http://www.codeskulptor.org/#user6-UbZVApbT6ahIJnI.py
#   in which I added a mini-map and increased the frame rate.
#
# v1.0: http://www.codeskulptor.org/#user6-oD2uRenZ5yXlpWp.py
#
# There are a few important points:
#
# The game requires a moderately quick computer to run at an acceptable rate, and I strongly recommend
# running it in Chrome rather than Firefox. In Chrome, I get a steady 20fps (v1.1), which is fine,
# whereas in Firefox I get 5fps which is unplayable.
#
# To add additional opponents, simply add names to the PLAYERS array defined at the top of the code.
#
# It's also straightforward to create your own tracks. The pre-defined tracks are defined inside a
# routine called _define_tracks() and consist of pairs of coordinates and tangent vectors, collectively
# called "control points". Search the web for "Hermite Curves" for more information.
#
# Apologies for the single character indents, but this was necessary to reduce code size since I
# exceeded CodeSkulptor's 64k limit.
#
# The game loads several images when it starts. Sometimes, an image inexplicably doesn't get loaded
# and so the game will keep telling you that it is waiting for images to load. If this happens, the
# easiest thing is just to restart the game.
#
# Burn rubber!

import math
import random
import simplegui
import time

# Player Roster - Feel free to add more names to this list.
# You always control the first player, and they are always placed last on the starting grid.
PLAYERS = (
 'Racer X',
 'Joe',
 'Scott',
 'John',
 'Stephen'
)

# Image Constants
IMAGES = (
 'racerx',
 'jwarren',
 'srixner',
 'jgreiner',
 'swong',
 'logo',
 'log',
 'gravel',
 'sand',
 'rock',
 'start_line',
 'start',
 'backdrop.jpg',
 ('banner', (1, 0.479)),
 ('tree_1', (5.94, 9.3)),
 ('tree_2', (6.59, 7.52)),
 ('tree_3', (5.73, 12)),
 ('tree_4', (7.4, 7.4)),
 ('tree_5', (6.2, 8.7)),
 ('tree_6', (2.5, 5.4)),
 'car_1',
 'car_2',
 'car_3',
 'car_4',
)

IMG_HEAD = 0
IMG_LOGO = 5
IMG_LOG = 6
IMG_GRAVEL = 7
IMG_SAND = 8
IMG_ROCK = 9
IMG_START_LINE = 10
IMG_START = 11
IMG_BACKDROP = 12
IMG_BANNER = 13
IMG_TREE = 14
IMG_CAR = 20

# Music Constants
MUSIC_TRACKS = (
 ('menu', 75),
 'start',
 'win',
 'lose',
 ('race1', 50.717),
 ('race2', 68.246)
)

MUSIC_MENU = 0
MUSIC_START = 1
MUSIC_WIN = 2
MUSIC_LOSE = 3
MUSIC_RACE = 4

# Asset Constants
ASSET_BASE = 'http://commondatastorage.googleapis.com/codeskulptor-demos/riceracer_assets/'
IMAGE_BASE = ASSET_BASE + 'img/'
IMAGE_TYPE = '.png'
MUSIC_BASE = ASSET_BASE + 'music/'
MUSIC_TYPE = '.ogg'
SFX_BASE = ASSET_BASE + 'fx/'
SFX_TYPE = '.ogg'
SFX_VOLUME = 0.2

FONT_STYLE = 'sans-serif'

# Sanity saving constants
X = 0
Y = 1
Z = 2

def is_tuple(x):
 return 'tuple' in str(type(x))

# Classes

class Sort:
 # Quicksort a list of tuples whose first element is the sorted key
 def quick_sort(list):
  if list == []:
   return []
  else:
   pivot = list[0]
   pivot_value = pivot[0]
   lesser = Sort.quick_sort([x for x in list[1 :] if x[0] < pivot_value])
   greater = Sort.quick_sort([x for x in list[1 :] if x[0] >= pivot_value])
   return lesser + [pivot] + greater

# A class to keep track of time intervals and provide an average of them
class TimeCounter:
 MAX_INTERVALS = 5

 def __init__(self):
  self.reset()

 def __str__(self):
  return str(self.intervals)

 def record_time(self):
  current_time = time.time()
  if self.last_time > 0:
   interval = current_time - self.last_time
   if len(self.intervals) < TimeCounter.MAX_INTERVALS:
    self.intervals.append(0)
   self.intervals[self.index] = interval
   self.index = (self.index + 1) % TimeCounter.MAX_INTERVALS
  else:
   self.initial_time = current_time
  self.last_time = current_time
  self.last_average_time = 0

 def get_average_time(self):
  if self.last_average_time != 0:
   return self.last_average_time

  total = 0
  l = len(self.intervals)
  if l > 0:
   for interval in self.intervals:
    total += interval
   total /= l

  self.last_average_time = total
  return total

 def get_current_time(self):
  return self.last_time

 def get_total_time(self):
  return self.last_time - self.initial_time

 def reset(self):
  self.intervals = []
  self.index = 0
  self.last_time = 0
  self.last_average_time = 0
  self.initial_time = 0

# Utility methods relating to maths
class Math:
 METRES_PER_SECOND_TO_MILES_PER_HOUR = 2.237

 # Define a rectangle in the form suitable for the polygon function
 def rect(x, y, w, h):
  return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]

 # Normalises a 3d vector
 def normalise(v):
  magnitude = math.sqrt((v[X] ** 2) + (v[Y] ** 2) + (v[Z] ** 2))
  return [v[0] / magnitude, v[1] / magnitude, v[2] / magnitude]

 # Returns the squared distance between two points
 def distance_sq(p1, p2):
  return (p1[X] - p2[X]) ** 2 + (p1[Y] - p2[Y]) ** 2 + (p1[Z] - p2[Z]) ** 2

 # Returns the distance between two points
 def distance(p1, p2):
  return math.sqrt(Math.distance_sq(p1, p2))

 # Linearly calculates a value between two values based on t (0 <= t <= 1)
 def interpolate(t, v1, v2):
  return v1 + t * (v2 - v1)

 def get_orientation_from_tangent_vector(t):
  return math.atan2(t[X], t[Z])

 def get_angle_between_orientations(o1, o2):
  angle = o2 - o1
  if abs(angle) > math.pi:
   angle = 2 * math.pi - abs(angle)
  return angle

class BoundingBox:
 def __init__(self):
  self.box = None

 def __str__(self):
  return str(self.box)

 def add(self, point):
  if self.box == None:
   # If this is the first point to be added to the box, then initialise the box extents based on it
   self.box = []
   for i in range(2):
    self.box.append(list(point))
   return

  # Grow the box to accommodate the new point
  min_pt = self.box[0]
  for a in range(3):
   if point[a] < min_pt[a]:
    min_pt[a] = point[a]
  max_pt = self.box[1]
  for a in range(3):
   if point[a] > max_pt[a]:
    max_pt[a] = point[a]

 def get_centre(self):
  b = self.box
  return ((b[1][X] + b[0][X]) / 2.0, (b[1][Y] + b[0][Y]) / 2.0, (b[1][Z] + b[0][Z]) / 2.0)

 def get_extent(self, axis):
  return self.box[1][axis] - self.box[0][axis]

class ImageManager:
 def __init__(self):
  self.images = []
  for image_data in IMAGES:
   image_name = image_data[0] if is_tuple(image_data) else image_data
   image_url = IMAGE_BASE + image_name
   if '.' not in image_name:
    image_url += IMAGE_TYPE
   self.images.append(simplegui.load_image(image_url))

 def get_number_of_pending_images(self):
  count = 0
  for image in self.images:
   if image.get_width() == 0:
    count += 1
  return count

class MusicTrack:
 def __init__(self, name, length):
  self.name = name
  self.length = length
  self.sound = simplegui.load_sound(MUSIC_BASE + name + MUSIC_TYPE);

class MusicManager:
 def __init__(self, time_counter):
  self.time_counter = time_counter
  self.active_track = -1
  self.selected_track = -1
  self.tracks = []
  self.mute = False
  for track in MUSIC_TRACKS:
   name = track[0] if is_tuple(track) else track
   length = track[1] if is_tuple(track) else 0
   self.tracks.append(MusicTrack(name, length))

 def play(self, track_index):
  self.stop()
  self.active_track = track_index;
  self.selected_track = track_index;
  self.sound_start_time = self.time_counter.get_current_time()
  track = self.tracks[track_index];
  track.sound.rewind()
  if not self.mute:
   track.sound.play()

 def stop(self):
  if self.active_track >= 0:
   self.tracks[self.active_track].sound.rewind()
  self.active_track = -1

 def process_sound(self):
  if self.active_track >= 0:
   track = self.tracks[self.active_track]
   if track.length > 0:
    current_time = self.time_counter.get_current_time()
    if current_time - self.sound_start_time >= track.length:
     self.play(self.active_track)

 def toggle(self):
  self.mute = not self.mute
  if self.mute:
   self.stop()
  else:
   self.play(self.selected_track)

class EngineManager:
 INTERVALS = 12
 SAMPLE_LENGTH_S = 11.436
 FUDGE_FACTOR_S = 0.2

 def __init__(self, time_counter):
  self.time_counter = time_counter
  self.active_sound = -1
  self.desired_sound = -1
  self.sounds = []
  self.sound_lengths = []
  self.mute = False
  length = EngineManager.SAMPLE_LENGTH_S
  factor = 2.0 ** (1.0 / 12.0)
  for i in range(1, EngineManager.INTERVALS + 1):
   sound_url = SFX_BASE + 'engine-' + str(i) + SFX_TYPE
   sound = simplegui.load_sound(sound_url)
   sound.set_volume(SFX_VOLUME)
   self.sounds.append(sound)
   self.sound_lengths.append(length)
   length /= factor

 def process_sound(self):
  if self.mute:
   return
  has_active_sound = self.active_sound >= 0
  current_time = self.time_counter.get_current_time()
  if self.desired_sound != self.active_sound:
   self.sounds[self.desired_sound].play()
   if has_active_sound:
    self.sounds[self.active_sound].rewind()
   self.active_sound = self.desired_sound
   self.sound_start_time = current_time
  elif has_active_sound:
   elapsed = current_time - self.sound_start_time
   if elapsed + EngineManager.FUDGE_FACTOR_S >= self.sound_lengths[self.active_sound]:
    self.sounds[self.active_sound].rewind()
    self.sounds[self.active_sound].play()
    self.sound_start_time = current_time

 def set_pitch(self, pitch):
  intervals = EngineManager.INTERVALS
  self.desired_sound = int(max(0, min(pitch * intervals, intervals - 1)))

 def stop(self):
  self.desired_sound = -1
  if self.active_sound >= 0:
   self.sounds[ self.active_sound ].rewind()
   self.active_sound = -1

 def toggle(self):
  self.mute = not self.mute
  if self.mute:
   self.stop()

class Player:
 HUMAN = 0
 COMPUTER = 1

 def __init__(self, name):
  # Work around bug in CodeSkulptor that doesn't allow 0 class members.
  Player.HUMAN = 0

  self.name = name
  self.reset()

 def reset(self):
  self.position = [0, 0]
  self.velocity = [0, 0]
  self.acceleration = [0, 0]

 def get_track_position_in_metres(self):
  return self.position[1] * TrackDef.DISTANCE_BETWEEN_SEGMENTS_M

class Sprite:
 ORIENTATION_BILLBOARD = 10000

 def __init__(self, position, size, orientation, image):
  self.position = position
  self.size = size
  self.orientation = orientation
  self.image = image

class HermiteCurve:
 HERMITE_BASE = ((2, -3, 0, 1), (-2, 3, 0, 0), (1, -2, 1, 0), (1, -1, 0, 0))
 HERMITE_DERIVATIVE = ((6, -6, 0, 0), (-6, 6, 0, 0), (3, -4, 1, 0), (3, -2, 0, 0))

 # Intiialise and create the coefficients for interpolating a Hermite curve
 # Parameters are: p1, p2 - Start and End points of the curve
 #      : t1, t2 - Tangent Vectors at the start and end of the curve
 def __init__(self, p1, p2, t1, t2):
  geometry = (p1, p2, t1, t2)
  self.coefs = []
  self.deriv_coefs = []
  for axis in range(3):
   coef = []
   deriv_coef = []
   for j in range(4):
    tot = 0
    deriv_tot = 0
    for k in range(4):
     tot += HermiteCurve.HERMITE_BASE[k][j] * geometry[k][axis]
     deriv_tot += HermiteCurve.HERMITE_DERIVATIVE[k][j] * geometry[k][axis]
    coef.append(tot)
    deriv_coef.append(deriv_tot)
   self.coefs.append(coef)
   self.deriv_coefs.append(deriv_coef)

 # Calculate a point on a 3d-curve using the coefficients previously calculated and t, where 0 <= t <= 1
 def calculate_point(self, t):
  t2 = t * t
  t3 = t2 * t
  p = []
  for i in range(3):
   c = self.coefs[i]
   p.append(c[0] * t3 + c[1] * t2 + c[2] * t + c[3])
  return p

 # Calculate the tangent vector at a point on the 3rd-curve
 def calculate_tangent(self, t):
  t2 = t * t
  p = []
  for i in range(3):
   c = self.deriv_coefs[i]
   p.append(c[0] * t2 + c[1] * t + c[2])
  return p

class TrackSegment:
 def __init__(self, position, orientation, image_name):
  self.position = position
  self.orientation = orientation
  self.sprite = Sprite(position, TrackDef.TRACK_SIZE_M, orientation, image_name)

class ControlPoint:
 def __init__(self, position, vector, image_name = None):
  self.position = position
  self.vector = vector
  self.image_name = image_name
  self.curve = None

class TrackDef:
 DEFAULT_GROUND_IMAGE = IMG_GRAVEL
 DEFAULT_ELEVATED_IMAGE = IMG_LOG

 DISTANCE_BETWEEN_SEGMENTS_M = 0.4

 TRACK_SIZE_M = (5, 0.7, DISTANCE_BETWEEN_SEGMENTS_M)

 def __init__(self, name, laps):
  self.name = name
  self.laps = laps
  self.control_points = []
  self.track = None
  self.bounding_box = BoundingBox()

 def add(self, control_point):
  self.control_points.append(control_point)

 # Returns the angle of the bend of the track at the specified position, in radians.
 def get_track_angle(self, position):
  track_index = int(position)
  track_length = len(self.track)
  track1 = self.track[track_index % track_length]
  track2 = self.track[(track_index + 1) % track_length]
  return Math.get_angle_between_orientations(track1.orientation, track2.orientation)

 def get_length_m(self):
  return len(self.track) * TrackDef.DISTANCE_BETWEEN_SEGMENTS_M

 # Create Track
 # Takes the control points specified in the track_def array and creates curves from them.
 def create_track(self):
  self.track = []
  track_def = self.control_points

  ground_level = 0.02

  # Store the starting point
  current_point = track_def[0].position

  # Distance in metres between each step on the curve
  max_distance = TrackDef.DISTANCE_BETWEEN_SEGMENTS_M

  current_ground_image = TrackDef.DEFAULT_GROUND_IMAGE
  current_elevated_image = TrackDef.DEFAULT_ELEVATED_IMAGE

  i = 0
  l = len(track_def)
  while i < l:
   # cp1 = Start Control Point. cp2 = End Control Point
   cp1 = track_def[i]
   i += 1
   cp2 = track_def[i % l]

   # Apply image for this track section
   if cp1.image_name != None:
    if cp1.position[Y] <= ground_level:
     current_ground_image = cp1.image_name
    else:
     current_elevated_image = cp1.image_name

   # Initialise object for curve calculations
   cp1.curve = HermiteCurve(cp1.position, cp2.position, cp1.vector, cp2.vector)

   # Estimate roughly how many line segments to break the curve into
   lines = Math.distance(cp1.position, cp2.position) * math.pi / (4 * max_distance)

   j = 1.0
   while j <= lines:
    t = j / lines
    next_point = cp1.curve.calculate_point(t)
    current_distance = Math.distance(current_point, next_point)
    if current_distance >= max_distance:
     dt = max_distance / current_distance
     vector = []
     new_point = []
     for a in range(3):
      vector.append(next_point[a] - current_point[a])
      new_point.append(current_point[a] + vector[a] * dt)
     orientation = Math.get_orientation_from_tangent_vector(vector)

     current_point = tuple(new_point)

     # Calculate track image
     if len(self.track) == 0:
      image_name = IMG_START_LINE
     elif current_point[Y] <= ground_level:
      image_name = current_ground_image
     else:
      image_name = current_elevated_image

     self.track.append(TrackSegment(current_point, orientation, image_name))
     self.bounding_box.add(current_point)
    else:
     j += 1

class Camera:
 def __init__(self):
  self.position = [0, 0, 0]
  self.set_yaw(0)
  self.set_pitch(0)
  self.set_roll(0)
  self._vbuff = [[0, 0, 0], [0, 0, 0]]

 def __str__(self):
  return str(self.position) + " [Yaw=" + str(round(self.yaw, 3)) + ", Roll=" + str(round(self.roll, 3)) + "]"

 def set_yaw(self, yaw):
  self.yaw = yaw
  self.sine_yaw = math.sin(yaw)
  self.cosine_yaw = math.cos(yaw)

 def set_pitch(self, pitch):
  self.pitch = pitch
  self.sine_pitch = math.sin(pitch)
  self.cosine_pitch = math.cos(pitch)

 def set_roll(self, roll):
  self.roll = roll
  self.sine_roll = math.sin(roll)
  self.cosine_roll = math.cos(roll)

 # Transformations
 def world_to_view(self, pos):
  # Translate pos from world coordinates into view coordinates (relative to camera)
  vbx = pos[0] - self.position[0]
  vby = pos[1] - self.position[1]
  vbz = pos[2] - self.position[2]

  # Rotate the view coordinates according to the camera's yaw
  vbx, vbz = vbx * self.cosine_yaw - vbz * self.sine_yaw, vbx * self.sine_yaw + vbz * self.cosine_yaw

  # This saves a bit of time during the game when pitch isn't used
  if self.pitch != 0:
   # Rotate the view coordinates according to the camera's pitch
   vby, vbz = vby * self.cosine_pitch - vbz * self.sine_pitch, vby * self.sine_pitch + vbz * self.cosine_pitch

  return (vbx, vby, vbz)

class Mechanics:
 CAR_SIZE_M = (1, 0.7, 0.5)
 CAR_VELOCITY_MAX_MS = (14, 45)
 CAR_ACCELERATION_MSS = (80, 30)
 CAR_DECELERATION_FACTOR = 2.5
 CAR_CENTRIFUGAL_MSS = 80
 CAR_VELOCITY_DAMPEN = (0.9, 0.96)
 CAR_VELOCITY_DAMPEN_TRACK_EDGE = 0.85
 COLLISION_DAMPEN = 0.9
 COLLISION_RELAXATION = 0.8

 def __init__(self, race):
  self.race = race

 # Simulate centrifugal force being applied to the human player as they take corners
 def apply_force(self):
  player = self.race.players[Player.HUMAN]
  vel = player.velocity
  acc = player.acceleration
  track_angle = self.race.track_def.get_track_angle(player.position[1])
  acc[0] -= vel[1] * track_angle * Mechanics.CAR_CENTRIFUGAL_MSS

 def move_players(self, delta):
  position_along_track_factor = delta / TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
  car_vel_max = Mechanics.CAR_VELOCITY_MAX_MS
  acc_factor = [0, 0]
  for player in self.race.players:
   pos = player.position
   vel = player.velocity
   acc = player.acceleration

   # Update Position. pos[1] is not measured in metres, which is why it must be multipled by position_factor_along_track
   pos[0] += vel[0] * delta
   pos[1] += vel[1] * position_along_track_factor

   # Calculate lateral acceleration strength based on forward velocity
   acc_factor[0] = min(2 * vel[1] / car_vel_max[1], 1)

   # Calculate forward acceleration strength - this gives greater acceleration at lower speeds and boosts deceleration
   if acc[1] > 0:
    acc_factor[1] = math.cos(vel[1] / car_vel_max[1] * math.pi / 2)
   else:
    acc_factor[1] = Mechanics.CAR_DECELERATION_FACTOR

   # Update Velocity
   vel[0] += acc[0] * delta * acc_factor[0]
   vel[1] += acc[1] * delta * acc_factor[1]

   # Constrain Velocity
   if vel[1] < 0:
    vel[1] = 0
   elif vel[1] > car_vel_max[1]:
    vel[1] = car_vel_max[1]
   if vel[0] < -car_vel_max[0]:
    vel[0] = -car_vel_max[0]
   elif vel[0] > car_vel_max[0]:
    vel[0] = car_vel_max[0]

   # Dampen velocity
   if acc[0] == 0 or vel[1] < 10:
    vel[0] *= Mechanics.CAR_VELOCITY_DAMPEN[0]
   if acc[1] == 0:
    vel[1] *= Mechanics.CAR_VELOCITY_DAMPEN[1]

 def process_collisions(self):
  players = self.race.players
  bb = []
  for player in players:
   bb.append(self._get_bounding_box(player))

  l = len(players)
  for i in range(l):
   p1 = players[i]
   bb1 = bb[i]
   for j in range(i + 1, l):
    p2 = players[j]
    bb2 = bb[j]

    dx0 = bb2[1][X] - bb1[0][X]
    if dx0 < 0:
     continue
    dx1 = bb1[1][X] - bb2[0][X]
    if dx1 < 0:
     continue
    dz0 = bb2[1][Y] - bb1[0][Y]
    if dz0 < 0:
     continue
    dz1 = bb1[1][Y] - bb2[0][Y]
    if dz1 < 0:
     continue

    # There has been a collision
    mtd_x = dx0 if dx0 < dx1 else -dx1
    mtd_z = dz0 if dz0 < dz1 else -dz1
    if abs(mtd_x) < abs(mtd_z):
     mtd_z = 0
    else:
     mtd_x = 0

    # Intersection Response - Separate the objects so that they just touch each other
    relaxation = Mechanics.COLLISION_RELAXATION
    fx = mtd_x * 0.5 * relaxation
    fz = mtd_z * 0.5 * relaxation / TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
    p1.position[X] += fx
    p1.position[Y] += fz
    p2.position[X] -= fx
    p2.position[Y] -= fz

    # Swap and dampen velocities if hitting back to front
    if mtd_z != 0:
     dampen = Mechanics.COLLISION_DAMPEN
     v = p1.velocity[Y]
     p1.velocity[Y] = p2.velocity[Y] * dampen
     p2.velocity[Y] = v * 0.9

 def constrain_players_to_track(self):
  car_half_width = Mechanics.CAR_SIZE_M[0] / 2
  track_half_width = TrackDef.TRACK_SIZE_M[0] / 2
  track_edge = (-track_half_width, track_half_width)
  for player in self.race.players:
   # Check if player is touching the edge of the track
   x = player.position[0]
   hit = False
   if x - car_half_width < track_edge[0]:
    x = track_edge[0] + car_half_width
    hit = True
   elif x + car_half_width > track_edge[1]:
    x = track_edge[1] - car_half_width
    hit = True
   if hit:
    player.position[0] = x
    player.velocity[0] = 0
    player.velocity[1] *= Mechanics.CAR_VELOCITY_DAMPEN_TRACK_EDGE

 # Returns a 2d bounding box for a player in 'track space', which is conceptually
 #   an infinitely long line whose origin is at the start of the race.
 def _get_bounding_box(self, player):
  pos = player.position
  hx = Mechanics.CAR_SIZE_M[X] / 2.0
  hz = Mechanics.CAR_SIZE_M[Z] / 2.0
  cx = pos[0]
  cz = pos[1] * TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
  return ((cx - hx, cz - hz), (cx + hx, cz + hz))

class Intelligence:
 class PlayerState:
  OVERTAKING_DISTANCE_M = 6
  LATERAL_SHUFFLE_MS = Mechanics.CAR_VELOCITY_MAX_MS[0] * 0.4

  def __init__(self, race, player):
   self.race = race
   self.player = player
   self.target_x = player.position[0]
   self.aggression = 0.9
   self.evaluate_count = 0
   self.think(player, player)

  def think(self, player_ahead, player_behind):
   self._calculate_relative_positions(player_ahead, player_behind)
   self._consider_overtaking(player_ahead, player_behind)
   self._apply_forward_acceleration()
   self._apply_lateral_velocity()

   self.evaluate_count -= 1
   if self.evaluate_count <= 0:
    if not self.close_to_player_behind and not self.close_to_player_ahead:
     available_width = (TrackDef.TRACK_SIZE_M[X] - Mechanics.CAR_SIZE_M[X]) * 0.4
     self.target_x = (random.random() * available_width) - (available_width / 2.0)
    self.aggression = max(min(self.aggression + random.random() * 0.04 - 0.02, 1), 0)
    self.evaluate_count = random.randrange(60) + 60

  def _apply_forward_acceleration(self):
   target_velocity = self._calculate_target_velocity()
   actual_velocity = self.player.velocity[1]
   acceleration_factor = 1 if target_velocity > actual_velocity else -Mechanics.CAR_DECELERATION_FACTOR
   self.player.acceleration[1] = Mechanics.CAR_ACCELERATION_MSS[1] * acceleration_factor

  def _apply_lateral_velocity(self):
   target_x = self.target_x
   actual_x = self.player.position[0]
   difference = target_x - actual_x
   if abs(difference) > 0.1:
    shuffle_factor = Intelligence.PlayerState.LATERAL_SHUFFLE_MS
    if difference < 0:
     shuffle_factor = -shuffle_factor
   else:
    shuffle_factor = 0
   self.player.velocity[0] = shuffle_factor

  def _calculate_target_velocity(self):
   track = self.race.track_def.track
   track_length = len(track)

   position = self.player.position[1]
   track_index = int(position)
   track1 = track[track_index % track_length]
   track2 = track[(track_index + Intelligence.TRACK_LOOK_AHEAD) % track_length]

   track_angle = Math.get_angle_between_orientations(track1.orientation, track2.orientation)
   target_velocity = Mechanics.CAR_VELOCITY_MAX_MS[1] * math.cos(min(abs(track_angle) * 1.4, 1)) * self.aggression
   return target_velocity

  def _calculate_relative_positions(self, player_ahead, player_behind):
   track_length = len(self.race.track_def.track)

   # See how close we are to the car in front and the car behind
   distance_to_player = int(player_ahead.position[1] - self.player.position[1])
   distance_to_player %= track_length
   distance_to_player *= TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
   self.close_to_player_ahead = (distance_to_player <= Intelligence.PlayerState.OVERTAKING_DISTANCE_M)

   # Make sure that we have cleared the car behind before making a manoeuvre
   distance_to_player = int(self.player.position[1] - player_behind.position[1])
   distance_to_player %= track_length
   distance_to_player *= TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
   self.close_to_player_behind = (distance_to_player <= Mechanics.CAR_SIZE_M[Z] * 2)

  def _consider_overtaking(self, player_ahead, player_behind):
   self.overtaking = None

   # Only consider overtaking if we are travelling faster than the player ahead of us
   if self.player.velocity[1] <= player_ahead.velocity[1]:
    return

   # Make sure that we are close enough to the car ahead to consider overtaking
   if not self.close_to_player_ahead:
    return

   # Make sure that we have cleared the car behind before making a manoeuvre
   if self.close_to_player_behind:
    return

   # We are going to position ourselves for overtaking
   self.overtaking = player_ahead

   opponent_x = player_ahead.position[0]
   car_double_width = 2 * Mechanics.CAR_SIZE_M[X]
   if opponent_x >= 0:
    target_x = opponent_x - car_double_width
    if target_x < self.target_x:
     self.target_x = target_x
   else:
    target_x = opponent_x + car_double_width
    if target_x > self.target_x:
     self.target_x = target_x

 # The number of track segments to look ahead to determine the appropriate velocity
 TRACK_LOOK_AHEAD = 10

 def __init__(self, race):
  self.race = race
  self.player_states = [Intelligence.PlayerState(race, player) for player in race.players]

 def process_players(self):
  track_length = len(self.race.track_def.track)

  # Create a list of players sorted by their position on the track, rather than their position in the race.
  # If all are on the same lap, this is the same thing, but otherwise it will be different.
  # This is necessary for players to work out who is physically in front or behind of them.
  players = []
  i = 0
  for player in self.race.players:
   players.append([player.position[1] - track_length * self.race.get_player_lap(player), i, player])
   i += 1
  sorted_players = Sort.quick_sort(players)

  i = 0
  l = len(sorted_players)
  while i < l:
   sorted_player = sorted_players[i]
   player_index = sorted_player[Race.SORTED_PLAYER_INDEX]
   if player_index != Player.HUMAN:
    player_state = self.player_states[player_index]
    player_ahead = sorted_players[(i + 1) % l][Race.SORTED_PLAYER_PLAYER]
    player_behind = sorted_players[(i - 1) % l][Race.SORTED_PLAYER_PLAYER]
    player_state.think(player_ahead, player_behind)
   i += 1

class Race:
 STARTING_GRID_SPACE_M = 1.2

 SORTED_PLAYER_POSITION = 0
 SORTED_PLAYER_INDEX = 1
 SORTED_PLAYER_PLAYER = 2

 # Initialise a Race specifying the players and the track definition
 def __init__(self, players, track_def):
  # Work around bug in CodeSkulptor that doesn't allow 0 class members.
  Race.SORTED_PLAYER_POSITION = 0

  self.players = players
  self.sorted_players = []
  self.track_def = track_def
  self.track_objects = [None] * len(track_def.track)
  self._dynamic_sprites = []
  self._create_track_objects()
  self._init_players()
  self._sort_players()
  self.mechanics = Mechanics(self)
  self.intelligence = Intelligence(self)

 # Initialise the players and position them on the starting grid
 def _init_players(self):
  offset = (TrackDef.TRACK_SIZE_M[X] / 4.0, -Race.STARTING_GRID_SPACE_M / TrackDef.DISTANCE_BETWEEN_SEGMENTS_M)
  x = (-offset[0], offset[0])
  z = offset[1]

  i = 0
  player_indices = range(Player.COMPUTER, len(self.players))
  random.shuffle(player_indices)

  # Ensure that the player starts at the rear of the grid
  player_indices.append(Player.HUMAN)
  for player_index in player_indices:
   player = self.players[player_index]
   player.reset()
   player.position[0] = x[i % 2]
   player.position[1] = z
   self.sorted_players.append([-z, player_index, player])
   i += 1
   z += offset[1]

 # Returns the 'lap' that a player is on
 def get_player_lap(self, player):
  return 1 + int(player.position[1] // len(self.track_def.track))

 # Returns the position in the race of the specified player
 def get_player_position(self, player_index):
  for i in range(len(self.sorted_players)):
   sorted_player = self.sorted_players[i]
   if sorted_player[Race.SORTED_PLAYER_INDEX] == player_index:
    return i + 1
  return 0

 # Returns a player's position on the track, from 0 at the start to len(track) at the end
 def get_player_track_position(self, player):
  track_position = player.position[1]
  track_length = len(self.track_def.track)
  while track_position < 0:
   track_position += track_length
  return track_position

 # Define all of the objects that decorate the track
 def _create_track_objects(self):
  track_width = TrackDef.TRACK_SIZE_M[X] * 1.2
  track_edge = track_width / 2

  # Create Starting Banner
  height = 2
  image_name = IMG_BANNER
  image_size = IMAGES[image_name][1]
  self._create_track_object(0, (0, height / 2, 0), (track_width, height), image_name)

  i = 0
  for segment in self.track_def.track:
   if random.randrange(4) == 0:
    tree = random.randrange(6)
    image_name = IMG_TREE + tree
    image_size = IMAGES[image_name][1]
    x = random.random() * 5 + track_edge
    y = image_size[1] / 2
    z = random.random()
    if random.randrange(2) == 0:
     x = -x
    self._create_track_object(i, (x, y, z), image_size, image_name, True)
   i += 1

 # Sorts the sorted_players list to reflect the relative positions of the players.
 def _sort_players(self):
  for sorted_player in self.sorted_players:
   sorted_player[Race.SORTED_PLAYER_POSITION] = -sorted_player[Race.SORTED_PLAYER_PLAYER].position[1]
  self.sorted_players = Sort.quick_sort(self.sorted_players)

 # Inserts a track object (a sprite associated with a particular position on the track)
 # The Sprite's position and orientation is relative to the track_position with which it is associated.
 def _create_track_object(self, track_position, position, size, image, absolute_y = False):
  track = self.track_def.track

  # Find the section of track with which this sprite will be associated
  track_index = int(track_position)
  modular_track_index = track_index % len(track)
  track1 = track[modular_track_index]
  track2 = track[(track_index + 1) % len(track)]

  # If track_position specifies a position between two segments of track, we need to
  #   interpolate the centre point and orientation
  t = track_position - track_index
  o1 = track1.orientation
  o2 = track2.orientation
  orientation = Math.interpolate(t, o1, o1 + Math.get_angle_between_orientations(o1, o2))
  centre = []
  for a in range(3):
   centre.append(Math.interpolate(t, track1.position[a], track2.position[a]))

  # Calculate world coordinates for the sprite, based on the centre of the track and the supplied coordinates
  sine = math.sin(orientation)
  cosine = math.cos(orientation)

  # Rotate the local coordinates according to the track segment's orientation
  px = position[X] * cosine + position[Z] * sine
  pz = position[Z] * cosine - position[X] * sine
  world_pos = (px + centre[X], position[Y] + (centre[Y] if not absolute_y else 0), pz + centre[Z])
  sprite = Sprite(world_pos, size, Sprite.ORIENTATION_BILLBOARD, image)

  # Check if sprites have already been assigned to this track_position
  sprite_bucket = self.track_objects[modular_track_index]
  if sprite_bucket != None:
   sprite_bucket.append(sprite)
  else:
   # Otherwise, start a new sprite bucket
   sprite_bucket = [sprite]
   self.track_objects[modular_track_index] = sprite_bucket

  # Return the bucket in which the sprite was added together with the index
  return (sprite_bucket, len(sprite_bucket) - 1)

 # Inserts sprites representing the players into the track_objects dictionary
 def add_player_sprites(self):
  # Calculate where the car appears above the track
  y = TrackDef.TRACK_SIZE_M[Y] / 2.0 + Mechanics.CAR_SIZE_M[Y] / 2.0
  for player in self.players:
   track_position = self.get_player_track_position(player)
   pos = (player.position[0], y, 0)
   frame = int(player.position[1] * 8) % 4
   self.add_dynamic_sprite(track_position, pos, Mechanics.CAR_SIZE_M, IMG_CAR + frame)

 # Registers a dynamic sprite that will be associated with a part of the track and which can be removed at the end of the frame
 def add_dynamic_sprite(self, track_position, position, size, image):
  self._dynamic_sprites.append(self._create_track_object(track_position, position, size, image))

 # Removes sprites representing dynamic objects that were inserted just for this frame
 def remove_dynamic_sprites(self):
  i = len(self._dynamic_sprites) - 1
  while i >= 0:
   sprite_bucket_info = self._dynamic_sprites[i]
   sprite_bucket_info[0].pop(sprite_bucket_info[1])
   i -= 1
  self._dynamic_sprites = []

 # Process a slice of time in the race
 def process_tick(self, delta):
  m = self.mechanics
  m.apply_force()
  m.move_players(delta)
  m.process_collisions()
  m.constrain_players_to_track()
  self._sort_players()
  self.intelligence.process_players()

class Renderer:
 # Note, if changing anything here, please update the view_to_canvas() method, which
 # uses hard-coded values to gain extra speed, since it is such an important routine.
 CANVAS_WIDTH = 800
 CANVAS_HEIGHT = 600
 CANVAS_HALF_WIDTH = CANVAS_WIDTH // 2
 CANVAS_HALF_HEIGHT = CANVAS_HEIGHT // 2
 SCALE_WIDTH = CANVAS_HALF_WIDTH
 SCALE_HEIGHT = CANVAS_HALF_HEIGHT
 NEAR_PLANE_M = 0.1
 FAR_PLANE_M = 200

 # Projects a 3d view-space coordinate into a 2d canvas coordinate
 # This routine is included as a reference, but is not used in the game.
 # Instead, see the method below it.
 def view_to_canvas_slow(pos):
  distance = pos[Z] + Renderer.NEAR_PLANE_M
  x = pos[X] / distance
  y = -pos[Y] / distance
  x *= Renderer.SCALE_WIDTH
  y *= Renderer.SCALE_HEIGHT
  x += Renderer.CANVAS_HALF_WIDTH
  y += Renderer.CANVAS_HALF_HEIGHT
  return (x, y)

 # Projects a 3d view-space coordinate into a 2d canvas coordinate
 # This is the optimised version of the view_to_canvas method.
 # It runs about twice as quickly as the 'readable' version.
 def view_to_canvas(pos):
  distance = pos[2] + 0.1
  return (400.0 * (pos[0] / distance + 1), 300.0 * (-pos[1] / distance + 1))

 def render_shadow_text(canvas, text, position, size, colour, shadow_colour = "#000"):
  canvas.draw_text(text, (position[0] + 2, position[1] + 2), size, shadow_colour, FONT_STYLE)
  canvas.draw_text(text, position, size, colour, FONT_STYLE)

 def render_image(canvas, image, pos):
  size = (image.get_width(), image.get_height())
  centre = (size[0] / 2, size[1] / 2)
  canvas.draw_image(image, centre, size, (pos[0] + centre[0], pos[1] + centre[1]), size)

class FPSRenderer(Renderer):
 def __init__(self, time_counter):
  self.time_counter = time_counter

 def render_fps(self, canvas):
  delta = self.time_counter.get_average_time()
  if delta > 0:
   fps = 1.0 / delta
   canvas.draw_text("FPS: " + str(int(round(fps))), (10, Renderer.CANVAS_HEIGHT - 10), 15, "#fff", FONT_STYLE)

class RaceRenderer(Renderer):
 class Message:
  def __init__(self, text, position):
   self.text = text
   self.position = position

 CAMERA_HEIGHT_ABOVE_TRACK_M = 1.1
 CAMERA_DISTANCE_BEHIND_PLAYER_M = 1.1

 TRACK_RENDER_MIN_DEPTH = 60   # The minimum amount of track segments to draw each frame
 COLOUR_BACKGROUND = "#22470b"
 COLOUR_ROSTER = "#fff"
 COLOUR_ROSTER_PLAYER = "#ff0"
 COLOUR_VELOCITY = "#ff0"

 def __init__(self, image_manager, race):
  self.camera = Camera()
  self.image_manager = image_manager
  self.race = race
  self.render_depth = RaceRenderer.TRACK_RENDER_MIN_DEPTH
  self.message = None

 def get_camera_track_position(self):
  track_position = self.race.get_player_track_position(self.race.players[Player.HUMAN])
  track_position -= RaceRenderer.CAMERA_DISTANCE_BEHIND_PLAYER_M / TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
  return track_position

 def _get_track(self):
  return self.race.track_def.track

 # Rotate 2d canvas coordinates about the centre of the screen based on the value of roll
 def _canvas_to_roll(self, pos):
  camera = self.camera
  cw = Renderer.CANVAS_HALF_WIDTH
  ch = Renderer.CANVAS_HALF_HEIGHT
  tx = pos[0] - cw
  ty = pos[1] - ch
  tx, ty = tx * camera.cosine_roll - ty * camera.sine_roll, tx * camera.sine_roll + ty * camera.cosine_roll
  return (tx + cw, ty + ch)

 def _render_background(self, canvas):
  c = self.camera

  # Calculate Horizon's y coordinate
  hy = -(RaceRenderer.CAMERA_HEIGHT_ABOVE_TRACK_M + c.position[Y])
  hz = Renderer.FAR_PLANE_M

  # Take into account the pitch of the camera
  horizon_vw = (0, hy * c.cosine_pitch - hz * c.sine_pitch, hy * c.sine_pitch + hz * c.cosine_pitch)
  horizon_cv = Renderer.view_to_canvas(horizon_vw)
  hy = horizon_cv[Y]

  # Draw Sky
  # The Sky image is 4480x360 pixels. The first 3200 are a panorama, then the first 1280 pixels are repeated.
  # Only 800 pixels ought to be repeated, but in order for the rolling effect to work, an additional margin is required.
  # The roll_factor is maximum amount of extra space needed in the upper margins when rolling.
  # Messy, but empirically ok when camera is pitching too. The original image height was 300, but 60 additional pixels added for margin.
  roll_factor = 1.7
  image = self.image_manager.images[IMG_BACKDROP]
  iw = 3200.0
  ih = 360.0
  if ih > 0:
   angle = (c.yaw + math.pi / 4.0)
   if c.yaw - abs(c.roll) < 0:
    angle += 2.0 * math.pi
   margin = abs(c.sine_roll) * ih * 2.0
   sp = (iw * angle / (math.pi * 2.0), ih / 2.0)
   ss = (iw / 4.0 + margin, ih)
   dih = ih * roll_factor
   dp = (Renderer.CANVAS_HALF_WIDTH, hy - dih / 2.0)
   ds = (ss[ 0 ], dih)
   dp = self._canvas_to_roll(dp)
   canvas.draw_image(image, sp, ss, dp, ds, c.roll)

 def _render_sprite(self, canvas, sprite):
  view_pos = self.camera.world_to_view(sprite.position)
  if (view_pos[Z] < Renderer.NEAR_PLANE_M) or (view_pos[Z] >= Renderer.FAR_PLANE_M):
   return

  centre = Renderer.view_to_canvas(view_pos)

  sprite_orientation = sprite.orientation
  if (sprite_orientation != Sprite.ORIENTATION_BILLBOARD):
   rotation = sprite_orientation - self.camera.yaw
   apparent_width = abs(sprite.size[X] * math.cos(rotation)) + abs(sprite.size[Z] * math.sin(rotation))
  else:
   apparent_width = sprite.size[X]

  horizontal_extent = Renderer.view_to_canvas((view_pos[X] - apparent_width / 2.0, view_pos[Y], view_pos[Z]))[X]
  vertical_extent = Renderer.view_to_canvas((view_pos[X], view_pos[Y] + sprite.size[Y] / 2.0, view_pos[Z]))[Y]
  width = (centre[X] - horizontal_extent) * 2.0
  height = (centre[Y] - vertical_extent) * 2.0

  # Rotate the centre point around the centre of the screen to simulate the roll effect
  centre = self._canvas_to_roll(centre)

  image = self.image_manager.images[sprite.image]
  image_size = (image.get_width(), image.get_height())
  if image_size[0] != 0:
   # Prevent images that didn't load from causing a crash
   image_centre = (image_size[0] / 2.0, image_size[1] / 2.0)
   canvas.draw_image(image, image_centre, image_size, centre, (width, height), self.camera.roll)

 # Render the track
 def _render_track(self, canvas):
  track = self._get_track()
  track_objects = self.race.track_objects
  track_length = len(track)
  length = max(min(self.render_depth, track_length), RaceRenderer.TRACK_RENDER_MIN_DEPTH)
  track_position = int(self.get_camera_track_position()) - 1
  for i in range(length):
   pos = (track_position + length - i) % track_length
   self._render_sprite(canvas, track[pos].sprite)

   sprite_bucket = track_objects[pos]
   if sprite_bucket != None:
    for sprite in sprite_bucket:
     self._render_sprite(canvas, sprite)

  self.render_depth = length

 # Render the roster of players
 def _render_player_roster(self, canvas):
  race = self.race
  x = 32
  xname = 56
  y = 50
  yd = 28

  height = yd * (len(race.players) + 0.5)

  rect = Math.rect(x - 12, y - yd, 320, height)
  colour = 'rgba(0,0,0,0.5)'
  canvas.draw_polygon(rect, 1, colour, colour)

  position = 1
  total_laps = race.track_def.laps
  for i in range(len(race.sorted_players)):
   sorted_player = race.sorted_players[i]
   player = sorted_player[Race.SORTED_PLAYER_PLAYER]
   lap = race.get_player_lap(player)
   message = str(position) + " - " + player.name + " - Lap " + str(lap) + " of " + str(total_laps)
   if i > 0:
    previous_player = race.sorted_players[i - 1][Race.SORTED_PLAYER_PLAYER]
    difference = previous_player.position[1] - player.position[1]
    difference_metres = difference * TrackDef.DISTANCE_BETWEEN_SEGMENTS_M
    message += " - " + str(round(difference_metres, 1)) + "m"

   index = sorted_player[Race.SORTED_PLAYER_INDEX]
   colour = RaceRenderer.COLOUR_ROSTER_PLAYER if index == Player.HUMAN else RaceRenderer.COLOUR_ROSTER
   canvas.draw_text(message, (xname, y), 16, colour, FONT_STYLE)
   if index < IMG_LOGO:
    Renderer.render_image(canvas, self.image_manager.images[IMG_HEAD + index], (x, y - 20))
   y += yd
   position += 1

 # Render the Player's position and speed
 def _render_player_status(self, canvas):
  velocity = self.race.players[Player.HUMAN].velocity[1] * Math.METRES_PER_SECOND_TO_MILES_PER_HOUR
  message = str(int(round(velocity)))

  x2 = Renderer.CANVAS_WIDTH - 60
  x1 = x2 - len(message) * 40
  y = Renderer.CANVAS_HEIGHT - 30
  Renderer.render_shadow_text(canvas, message, (x1, y), 60, RaceRenderer.COLOUR_VELOCITY)
  Renderer.render_shadow_text(canvas, "mph", (x2, y), 18, RaceRenderer.COLOUR_VELOCITY)

 def _render_message(self, canvas):
  if self.message == None:
   return
  Renderer.render_shadow_text(canvas, self.message.text, (self.message.position, Renderer.CANVAS_HEIGHT - 80), 24, "White", "Black")

 # Render the race
 def render(self, canvas):
  self._render_background(canvas)
  self._render_track(canvas)
  self._render_player_roster(canvas)
  self._render_player_status(canvas)
  self._render_message(canvas)

class MiniMapRenderer(Renderer):
 COLOUR_TRACK = "#000"
 COLOUR_PLAYER = "#f00"

 def __init__(self, race, rect):
  bbox = race.track_def.bounding_box
  self.race = race
  self.track_centre = bbox.get_centre()
  self.scale = min(rect[2] / bbox.get_extent(X), rect[3] / bbox.get_extent(Z))
  self.origin = (rect[0] + (rect[2] - bbox.get_extent(X) * self.scale) / 2, rect[1] - (rect[3] - bbox.get_extent(Z) * self.scale) / 2)
  self.points = []
  self._calculate_track()

 def _calculate_track(self):
  control_points = self.race.track_def.control_points
  lines_per_def = max(6, 80 / len(control_points))
  self.points = []
  for cp in control_points:
   for j in range(lines_per_def):
    self.points.append(self._project(cp.curve.calculate_point(float(j) / lines_per_def)))
  self.points.append(self.points[0])

 def _project(self, point):
  x = self.origin[0] + (point[X] - self.track_centre[X]) * self.scale
  y = self.origin[1] - (point[Z] - self.track_centre[Z]) * self.scale
  return (x, y)

 def render(self, canvas):
  canvas.draw_polyline(self.points, 8, MiniMapRenderer.COLOUR_TRACK)

  race = self.race
  track = race.track_def.track
  index = 1
  for sorted_player in self.race.sorted_players:
   player = sorted_player[Race.SORTED_PLAYER_PLAYER]
   player_position = self.race.get_player_track_position(player) % len(track)
   pos = self._project(track[int(player_position)].position)

   colour = RaceRenderer.COLOUR_ROSTER_PLAYER if sorted_player[Race.SORTED_PLAYER_INDEX] == Player.HUMAN else RaceRenderer.COLOUR_ROSTER
   canvas.draw_circle(pos, 3, 1, MiniMapRenderer.COLOUR_PLAYER, colour)
   canvas.draw_text(str(index), (pos[0] - 4, pos[1] - 8), 14, colour, FONT_STYLE)
   index += 1

class TrackOverviewRenderer(Renderer):
 COLOUR_TRACK_BASE = "#4a4a19"
 COLOUR_TRACK_BASE_OUTLINE = "#2fa206"
 COLOUR_TRACK = "#fef126"
 TRACK_HALF_WIDTH = TrackDef.TRACK_SIZE_M[0] / 2
 TRACK_POSITION = (Renderer.CANVAS_HALF_WIDTH / 2, Renderer.CANVAS_HALF_HEIGHT / 2)

 def __init__(self, track_def):
  self.track_def = track_def
  self.camera = Camera()
  self.camera.set_pitch(-math.pi * 45  / 180)
  self.points = None

  bb = self.track_def.bounding_box.box
  self.radius = max(bb[1][X] - bb[0][X], bb[1][Z] - bb[0][Z]) + 20
  self.track_centre = self.track_def.bounding_box.get_centre()
  self.camera.position[Y] = self.radius
  self.set_track_rotation(0)
  self._calculate_track()

 def set_track_rotation(self, theta):
  c = self.camera
  c.set_yaw(theta)
  c.position[X] = -self.radius * c.sine_yaw
  c.position[Z] = -self.radius * c.cosine_yaw

 def render(self, canvas):
  self._render_base(canvas)
  self._render_track(canvas)

 def _render_base(self, canvas):
  track_offset = TrackOverviewRenderer.TRACK_POSITION
  bb = self.track_def.bounding_box
  box = bb.box
  c = bb.get_centre()

  ts = 15 + TrackOverviewRenderer.TRACK_HALF_WIDTH
  y = box[0][Y] - c[Y]
  x1 = box[0][X] - c[X] - ts
  z1 = box[0][Z] - c[Z] - ts
  x2 = box[1][X] - c[X] + ts
  z2 = box[1][Z] - c[Z] + ts

  w = []
  w.append((x1, y, z1))
  w.append((x2, y, z1))
  w.append((x2, y, z2))
  w.append((x1, y, z2))

  v = []
  for p in w:
   vp = Renderer.view_to_canvas(self.camera.world_to_view(p))
   vp = (vp[0] + track_offset[0], vp[1] + track_offset[1])
   v.append(vp)
  v.append(v[0])
  canvas.draw_polygon(v, 3, TrackOverviewRenderer.COLOUR_TRACK_BASE_OUTLINE, TrackOverviewRenderer.COLOUR_TRACK_BASE)

 def _calculate_track(self):
  control_points = self.track_def.control_points
  lines_per_def = max(6, 80 / len(control_points))

  self.points = [[], []]
  for cp in control_points:
   for j in range(lines_per_def):
    t = float(j) / lines_per_def
    p = self._calculate_track_points(cp.curve, t)
    for e in range(2):
     self.points[e].append(p[e])

 def _calculate_track_points(self, curve, t):
  p = curve.calculate_point(t)
  p[X] -= self.track_centre[X]
  p[Y] -= self.track_centre[Y]
  p[Z] -= self.track_centre[Z]
  v = Math.normalise(curve.calculate_tangent(t))
  v[0] *= TrackOverviewRenderer.TRACK_HALF_WIDTH
  v[2] *= TrackOverviewRenderer.TRACK_HALF_WIDTH
  return ((p[X] - v[Z], p[Y], p[Z] + v[X]), (p[X] + v[Z], p[Y], p[Z] - v[X]))

 def _render_track(self, canvas):
  camera = self.camera
  track_offset = TrackOverviewRenderer.TRACK_POSITION

  start_line = []

  # Draw both edges of the track
  for e in range(2):
   points = []
   for p in self.points[e]:
    vp = Renderer.view_to_canvas(camera.world_to_view(p))
    vp = (vp[0] + track_offset[0], vp[1] + track_offset[1])
    points.append(vp)
   start_point = points[0]
   points.append(start_point)
   start_line.append(start_point)
   canvas.draw_polyline(points, 2, TrackOverviewRenderer.COLOUR_TRACK)

  # Draw Start / Finish Line
  canvas.draw_line(start_line[0], start_line[1], 2, TrackOverviewRenderer.COLOUR_TRACK)

class IntroRenderer(Renderer):
 COLOUR_BACKGROUND = "#312194"
 COLOUR_PANEL = "#1e155f"
 COLOUR_PANEL_EDGE = "#271c7c"
 COLOUR_TEXT_LABEL = "#fef126"
 COLOUR_TEXT_VALUE = "#fff"
 COLOUR_TEXT_ADVICE = "#ef9673"
 COLOUR_TEXT_LOADING = "#f00"

 def __init__(self, image_manager):
  self.image_manager = image_manager
  self.track_rotation = 0
  self.track = None

 def set_track(self, track):
  self.track = track
  self._track_renderer = TrackOverviewRenderer(track)

 def render(self, canvas):
  Renderer.render_image(canvas, self.image_manager.images[IMG_LOGO], (Renderer.CANVAS_HALF_WIDTH - 230, 16))
  if self.track:
   rect = Math.rect(40, Renderer.CANVAS_HALF_HEIGHT + 70, Renderer.CANVAS_WIDTH - 80, Renderer.CANVAS_HALF_HEIGHT - 120)
   canvas.draw_polygon(rect, 4, IntroRenderer.COLOUR_PANEL_EDGE, IntroRenderer.COLOUR_PANEL)

   self._track_renderer.set_track_rotation(self.track_rotation)
   self._track_renderer.render(canvas)

   Renderer.render_shadow_text(canvas, "Choose Track with LEFT and RIGHT", (Renderer.CANVAS_HALF_WIDTH - 155, Renderer.CANVAS_HALF_HEIGHT + 50), 18, IntroRenderer.COLOUR_TEXT_ADVICE)

   x1 = 70
   x2 = 190
   y = Renderer.CANVAS_HALF_HEIGHT + 125
   Renderer.render_shadow_text(canvas, "Track:", (x1, y), 22, IntroRenderer.COLOUR_TEXT_LABEL)
   Renderer.render_shadow_text(canvas, self.track.name, (x2, y), 22, IntroRenderer.COLOUR_TEXT_VALUE)

   y += 40
   laps = str(self.track.laps)
   Renderer.render_shadow_text(canvas, "Laps:", (x1, y), 22, IntroRenderer.COLOUR_TEXT_LABEL)
   Renderer.render_shadow_text(canvas, laps, (x2, y), 22, IntroRenderer.COLOUR_TEXT_VALUE)

   y += 40
   distance = str(int(round(self.track.get_length_m()))) + " metres"
   Renderer.render_shadow_text(canvas, "Distance:", (x1, y), 22, IntroRenderer.COLOUR_TEXT_LABEL)
   Renderer.render_shadow_text(canvas, distance, (x2, y), 22, IntroRenderer.COLOUR_TEXT_VALUE)

   pending_images = self.image_manager.get_number_of_pending_images()
   ready = (pending_images == 0)
   message = "Press SPACE to RACE!" if ready else "Waiting for " + str(pending_images) + " images"
   colour = IntroRenderer.COLOUR_TEXT_ADVICE if ready else IntroRenderer.COLOUR_TEXT_LOADING
   Renderer.render_shadow_text(canvas, message, (Renderer.CANVAS_HALF_WIDTH - 100, Renderer.CANVAS_HEIGHT - 18), 18, colour)

   Renderer.render_shadow_text(canvas, Game.VERSION, (Renderer.CANVAS_WIDTH - 130, 15), 13, IntroRenderer.COLOUR_TEXT_LABEL)
   Renderer.render_shadow_text(canvas, "'A' = Toggle Music", (Renderer.CANVAS_WIDTH - 124, Renderer.CANVAS_HEIGHT - 25), 14, IntroRenderer.COLOUR_TEXT_ADVICE)
   Renderer.render_shadow_text(canvas, "'S' = Toggle SFX", (Renderer.CANVAS_WIDTH - 124, Renderer.CANVAS_HEIGHT - 10), 14, IntroRenderer.COLOUR_TEXT_ADVICE)

class BuildTracksRenderer(Renderer):
 COLOUR_BACKGROUND = "#333"

 def __init__(self, game):
  self.game = game
  self.track_index = 0
  self.log = []

 def render(self, canvas):
  track_defs = self.game.track_defs
  if self.track_index < len(track_defs):
   track_def = track_defs[self.track_index];
   start_time = time.time()
   track_def.create_track()
   finish_time = time.time()
   self.log.append('Building track "' + track_def.name + '" ... ' + str(round(finish_time - start_time, 2)) + ' seconds')
   self.track_index += 1

   y = 50
   for line in self.log:
    canvas.draw_text(line, (50, y), 18, '#0a0', FONT_STYLE)
    y += 24
  else:
   self.game.show_introduction()

class Key:
 UP = simplegui.KEY_MAP['up']
 DOWN = simplegui.KEY_MAP['down']
 LEFT = simplegui.KEY_MAP['left']
 RIGHT = simplegui.KEY_MAP['right']
 SPACE = simplegui.KEY_MAP['space']
 MAP = simplegui.KEY_MAP['m']
 SFX = simplegui.KEY_MAP['s']
 MUSIC = simplegui.KEY_MAP['a']
 ESCAPE = 27

class Game:
 VERSION = 'v1.4 11th July 2013'

 STATE_INTRODUCTION = 1
 STATE_PRE_RACE = 2
 STATE_RACE = 3
 STATE_POST_RACE = 4
 STATE_BUILD_TRACKS = 5

 PRE_RACE_HEIGHT_M = 15
 PRE_RACE_DELAY_S = 3.5

 FPS = 60

 def __init__(self):
  self.state = Game.STATE_BUILD_TRACKS
  self.frame = simplegui.create_frame("Power Drift", Renderer.CANVAS_WIDTH, Renderer.CANVAS_HEIGHT)
  self.frame.set_draw_handler(self.on_render)
  self.frame.set_keydown_handler(self.on_keydown)
  self.frame.set_keyup_handler(self.on_keyup)
  self.frame.set_canvas_background(BuildTracksRenderer.COLOUR_BACKGROUND)
  self.frame.start()

  self.time_counter = TimeCounter()
  self.image_manager = ImageManager()
  self.music_manager = MusicManager(self.time_counter)
  self.engine_manager = EngineManager(self.time_counter)
  self.players = []
  self.track_defs = []
  self.active_keys = {}
  self._build_tracks_renderer = BuildTracksRenderer(self)
  self._intro_renderer = IntroRenderer(self.image_manager)
  self._fps_renderer = FPSRenderer(self.time_counter)
  self._race_renderer = None
  self._map_renderer = None
  self._show_map = True
  self._define_players()
  self._define_tracks()

 # Define Players
 def _define_players(self):
  for name in PLAYERS:
   self.players.append(Player(name))

 # Define Track
 # A Track is defined as a list of control points and their tangent vectors.
 def _define_tracks(self):
  t = TrackDef('Infinity', 3)
  t.add(ControlPoint((7, 0, -84), (5, 0, 20)))
  t.add(ControlPoint((21, 0, -13), (5, 0, 35)))
  t.add(ControlPoint((13, 0, 0), (-20, 0, 0)))
  t.add(ControlPoint((4, 0, -13), (0, 0, -20)))
  t.add(ControlPoint((8, 0, -26), (10, 0, -25)))
  t.add(ControlPoint((14, 7, -52), (5, -2, -25)))
  t.add(ControlPoint((17, 3, -64), (5, 3, -25)))
  t.add(ControlPoint((22, 9, -79), (5, -2, -15)))
  t.add(ControlPoint((27, 0, -100), (2, 0, -10), IMG_SAND))
  t.add(ControlPoint((28, 0, -115), (0, 0, -30)))
  t.add(ControlPoint((16, 0, -140), (-30, 0, 0)))
  t.add(ControlPoint((4, 0, -115), (0, 0, 30)))
  self.track_defs.append(t)

  t = TrackDef('Orion', 4)
  m = 40
  t.add(ControlPoint((0, 0, 20), (0, 0, m)))
  t.add(ControlPoint((20, 0, 40), (m, 0, 0), IMG_SAND))
  t.add(ControlPoint((40, 0, 20), (0, 0, -m), IMG_GRAVEL))
  t.add(ControlPoint((20, 0, 0), (-m, 0, 0)))
  t.add(ControlPoint((0, 4, 0), (-m, 0, 0)))
  t.add(ControlPoint((-20, 0, 0), (-m, 0, 0)))
  t.add(ControlPoint((-40, 0, -20), (0, 0, -m), IMG_SAND))
  t.add(ControlPoint((-20, 0, -40), (m, 0, 0), IMG_GRAVEL))
  t.add(ControlPoint((0, 0, -20), (0, 0, m)))
  self.track_defs.append(t)

  t = TrackDef('Saddle', 3)
  t.add(ControlPoint((107, 0, 37), (0, 0, -30)))
  t.add(ControlPoint((91, 0, 13), (-30, 0, 0)))
  t.add(ControlPoint((75, 0, 27), (-8, 0, 15), IMG_SAND))
  t.add(ControlPoint((57, 0, 39), (-30, 0, 0)))
  t.add(ControlPoint((39, 0, 27), (-8, 0, -15), IMG_GRAVEL))
  t.add(ControlPoint((23, 0, 13), (-30, 0, 0)))
  t.add(ControlPoint((7, 2, 37), (0, 10, 30)))
  t.add(ControlPoint((7, 5, 45), (0, 3, 10)))
  t.add(ControlPoint((7, 3, 52), (0, -3, 10)))
  t.add(ControlPoint((7, 5, 63), (0, 10, 10)))
  t.add(ControlPoint((23, 0, 87), (30, 0, 0)))
  t.add(ControlPoint((39, 0, 73), (8, 0, -15), IMG_SAND))
  t.add(ControlPoint((57, 0, 61), (30, 0, 0)))
  t.add(ControlPoint((75, 0, 73), (8, 0, 15), IMG_GRAVEL))
  t.add(ControlPoint((91, 0, 87), (30, 0, 0)))
  t.add(ControlPoint((107, 0, 63), (0, 0, -30)))
  self.track_defs.append(t)

  t = TrackDef('Tree-Tops', 4)
  t.add(ControlPoint((74, 0, 16), (12, 0, 10)))
  t.add(ControlPoint((86, 3, 39), (0, 0, 30)))
  t.add(ControlPoint((72, 1, 55), (-30, 0, 0)))
  t.add(ControlPoint((46, 4, 36), (-30, 0, 0)))
  t.add(ControlPoint((20, 1, 55), (-30, 0, 0)))
  t.add(ControlPoint((4, 3, 39), (0, 0, -30)))
  t.add(ControlPoint((18, 0, 16), (12, 0, -10)))
  t.add(ControlPoint((46, 2, 3), (40, 0, 0)))
  self.track_defs.append(t)

  t = TrackDef('Oval', 5)
  t.add(ControlPoint((0, 0, 0), (0, 0, 100)))
  t.add(ControlPoint((100, 0, 0), (0, 0, -100)))
  self.track_defs.append(t)

  t = TrackDef('Inside-Out', 3)
  t.add(ControlPoint((15, 0, 15), (25, 0, -30), IMG_ROCK))
  t.add(ControlPoint((55, 0, -10), (30, 0, 30)))
  t.add(ControlPoint((40, 0, 26), (-25, 0, 25)))
  t.add(ControlPoint((22, 2, 49), (0, 0, 25)))
  t.add(ControlPoint((35, 3, 65), (25, 0, 0)))
  t.add(ControlPoint((47, 2, 49), (0, 0, -25)))
  t.add(ControlPoint((64, 0, 27), (40, 0, 15)))
  t.add(ControlPoint((43, 0, 84), (-90, 0, 0)))
  self.track_defs.append(t)

  # Add your own tracks here...

 # Apply the player's input to their car's acceleration
 def _apply_input(self):
  acc = self.players[Player.HUMAN].acceleration
  car_acc = Mechanics.CAR_ACCELERATION_MSS
  acc[0] = (car_acc[0] if self.is_key_pressed(Key.RIGHT) else 0) + (-car_acc[0] if self.is_key_pressed(Key.LEFT) else 0)
  acc[1] = (car_acc[1] if self.is_key_pressed(Key.UP) else 0) + (-car_acc[1] if self.is_key_pressed(Key.DOWN) else 0)

 def _calculate_roll(self):
  desired_roll = 0
  strength = 0

  # Adjust roll based on player's applied horizontal acceleration and their forward velocity
  player = self.players[Player.HUMAN]
  acc = player.acceleration[0]
  if acc != 0:
   acc /= -Mechanics.CAR_ACCELERATION_MSS[0]
   vel = player.velocity[1] / Mechanics.CAR_VELOCITY_MAX_MS[1]
   strength = acc * vel
   desired_roll = strength * math.pi / 6

  c = self._race_renderer.camera
  actual_roll = c.roll

  if actual_roll != desired_roll:
   theta = math.pi / (70 if strength == 0 else 40)
   if actual_roll < desired_roll:
    actual_roll = min(actual_roll + theta, desired_roll)
   else:
    actual_roll = max(actual_roll - theta, desired_roll)
   c.set_roll(actual_roll)

 def _get_number_suffix(self, number):
  n = number % 10
  if n == 1 and number != 11:
   return 'st'
  if n == 2 and number != 12:
   return 'nd'
  if n == 3 and number != 13:
   return 'rd'
  return 'th'

 def is_key_pressed(self, key):
  return key in self.active_keys and self.active_keys[key] == True

 def _set_selected_track_index(self, index):
  index %= len(self.track_defs)
  self.selected_track_index = index
  self._intro_renderer.set_track(self.track_defs[index])

 def start_race(self, track_def):
  self.state = Game.STATE_PRE_RACE
  self.time_counter.reset()
  self.frame.set_canvas_background(RaceRenderer.COLOUR_BACKGROUND)
  self.race = Race(self.players, track_def)
  self._race_renderer = RaceRenderer(self.image_manager, self.race)
  self._race_renderer.message = RaceRenderer.Message('Use Cursor Keys to Accelerate, Brake and Steer', 150)
  self._map_renderer = MiniMapRenderer(self.race, (Renderer.CANVAS_WIDTH * 0.8, Renderer.CANVAS_HEIGHT * 0.2, Renderer.CANVAS_WIDTH * 0.3, Renderer.CANVAS_HEIGHT * 0.3))
  self.music_manager.play(MUSIC_START)

 def show_introduction(self):
  if self.state == Game.STATE_BUILD_TRACKS:
   self._set_selected_track_index(0)
  self.state = Game.STATE_INTRODUCTION
  self.frame.set_canvas_background(IntroRenderer.COLOUR_BACKGROUND)
  self.engine_manager.stop()
  self.music_manager.play(MUSIC_MENU)
  self.race = None
  self._race_renderer = None
  self._map_renderer = None

 # Position the camera behind the player's car, facing along the track
 def set_camera_position(self):
  race = self.race
  player = self.players[Player.HUMAN]
  track = race.track_def.track
  track_position = race.get_player_track_position(player)
  track_index = int(track_position)
  track1 = track[track_index % len(track)]
  track2 = track[(track_index + 1) % len(track)]

  t = track_position - track_index
  o1 = track1.orientation
  o2 = track2.orientation

  c = self._race_renderer.camera
  c.set_yaw(Math.interpolate(t, o1, o1 + Math.get_angle_between_orientations(o1, o2)))

  for a in range(3):
   c.position[a] = Math.interpolate(t, track1.position[a], track2.position[a])

  # Tilt and re-position the camera when going up and down hills
  ydiff = track2.position[Y] - track1.position[Y]
  c.set_pitch(ydiff * math.pi / 2)
  c.position[Y] += -ydiff * 5

  player_x = player.position[0]
  player_z = RaceRenderer.CAMERA_DISTANCE_BEHIND_PLAYER_M
  player_z += player.velocity[1] / Game.FPS
  c.position[X] += c.cosine_yaw * player_x - c.sine_yaw * player_z
  c.position[Y] += RaceRenderer.CAMERA_HEIGHT_ABOVE_TRACK_M
  c.position[Z] -= c.sine_yaw * player_x + c.cosine_yaw * player_z

  if self.state == Game.STATE_PRE_RACE:
   delta = self.time_counter.get_total_time() / Game.PRE_RACE_DELAY_S
   if delta < 1:
    c.position[Y] += Game.PRE_RACE_HEIGHT_M * (1 - delta)

    # Add "Start" sprite
    track_position = self._race_renderer.get_camera_track_position() + 1
    x = player.position[X]
    y = self._race_renderer.camera.position[Y] + 0.2
    z = 20 * (1 - delta)
    self.race.add_dynamic_sprite(track_position, (x, y, z), (4.43, 3.07), IMG_START)
   else:
    self.state = Game.STATE_RACE
    self.music_manager.play(MUSIC_RACE + self.selected_track_index % 2)
    self._race_renderer.message = None

 def process_tick(self):
  self.time_counter.record_time()
  delta = self.time_counter.get_average_time()
  self.music_manager.process_sound()

  if self.state != Game.STATE_INTRODUCTION:
   # Adjust render depth to try to maintain a frame rate around 30fps
   self._race_renderer.render_depth += 1 if delta < 0.031 else -1 if delta > 0.035 else 0

   if self.state == Game.STATE_RACE or self.state == Game.STATE_POST_RACE:
    self._apply_input()
    self._calculate_roll()

    race = self.race
    race.process_tick(1.0 / Game.FPS)

    self.engine_manager.set_pitch(self.players[Player.HUMAN].velocity[1] / Mechanics.CAR_VELOCITY_MAX_MS[1])
    self.engine_manager.process_sound()

    # Check if race has finished
    if self.state == Game.STATE_RACE:
     if race.get_player_lap(self.players[Player.HUMAN]) > race.track_def.laps:
      final_position = self.race.get_player_position(Player.HUMAN)
      suffix = self._get_number_suffix(final_position)
      message = 'You finished ' + str(final_position) + suffix + ' - Press ESC to race again'
      self.music_manager.play(MUSIC_WIN if final_position == 1 else MUSIC_LOSE)
      self._race_renderer.message = RaceRenderer.Message(message, 160)
      self.state = Game.STATE_POST_RACE
  else:
   # Rotate the track 60 degrees per second
   self._intro_renderer.track_rotation += delta * math.pi / 3

 def on_render(self, canvas):
  if self.state == Game.STATE_INTRODUCTION:
   self.process_tick()
   self._intro_renderer.render(canvas)
  elif self.state == Game.STATE_BUILD_TRACKS:
   self._build_tracks_renderer.render(canvas)
  else:
   self.process_tick()
   self.race.add_player_sprites()
   self.set_camera_position()
   self._race_renderer.render(canvas)
   if self._show_map:
    self._map_renderer.render(canvas)
   self.race.remove_dynamic_sprites()
  self._fps_renderer.render_fps(canvas)

 def on_keydown(self, key):
  self.active_keys[key] = True
  if self.state == Game.STATE_INTRODUCTION:
   if self.is_key_pressed(Key.LEFT):
    self._set_selected_track_index(self.selected_track_index - 1)
   elif self.is_key_pressed(Key.RIGHT):
    self._set_selected_track_index(self.selected_track_index + 1)
   elif self.is_key_pressed(Key.SPACE):
    self.start_race(self.track_defs[self.selected_track_index])
  elif self.state != Game.STATE_BUILD_TRACKS:
   if self.is_key_pressed(Key.ESCAPE):
    self.show_introduction()
  if self.is_key_pressed(Key.MAP):
   self._show_map = not self._show_map
  elif self.is_key_pressed(Key.SFX):
   self.engine_manager.toggle()
  elif self.is_key_pressed(Key.MUSIC):
   self.music_manager.toggle()

 def on_keyup(self, key):
  self.active_keys[key] = False

# Initialisation
Game()