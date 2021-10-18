from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

tickrate = 0.1
size = 7
gameObjects = []

class Vector2(object):
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)

class GameObject(object):
  def __init__(self, x, y, color):
    self.position = Vector2(x, y)
    self.color = color
    self.create()
  
  def create(self):
    gameObjects.append(self)
  
  def OnStart(self):
    pass
  
  def OnUpdate(self):
    pass

class Rigidbody(GameObject):
  def __init__(self, x, y, color, hasGravity):
    self.hasGravity = hasGravity
    super().__init__(x, y, color)
  
  def OnStart(self):
    self.velocity = Vector2(0, 0)
  
  def OnUpdate(self):
    if(self.hasGravity and self.position.x <= size and self.position.y <= size and self.position.x > 0 and self.position.y > 0):
      self.velocity.y = -1
      self.position.y += self.velocity.y

def start():
  s.clear()
  s.set_rotation(90)
  for obj in gameObjects:
    obj.OnStart()
  
  print(testObject.position.x, testObject.position.y)

def update():
  for obj in gameObjects:
    obj.OnUpdate()

def render():
  s.clear()
  for obj in gameObjects:
    if(obj.position.x <= size and obj.position.y <= size and obj.position.x >= 0 and obj.position.y >= 0):
      s.set_pixel(obj.position.x, obj.position.y, obj.color)

def tick():
  start()
  update()
  render()

testObject = Rigidbody(size, size, green, True)

while True:
  tick()
  time.sleep(tickrate)
  
