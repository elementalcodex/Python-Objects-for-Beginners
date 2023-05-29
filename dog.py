import sys
import time
from IPython.display import Audio, display
from PIL import Image
from random import randint as rint

class Dog:
  """ This is the Dog class.  It defines what a dog object is. \n 
  The value of a dog object is it's health, happiness, and energy."""
  def __init__(self):
    self.health = 50
    self.energy = 50
    self.happiness = 50
  def __str__(self):
    s = f'Dog\'s Status: \nHealth: {self.health}\nEnergy: {self.energy}\nHappiness: {self.happiness}'
    return s
  def sound(self, sound_name):
    display(Audio('/content/Python-Objects-for-Beginners/dogsounds/' + sound_name, autoplay=True))
    time.sleep(2)
  def image(self,img):
    i = Image.open('/content/Python-Objects-for-Beginners/dogpics/' + img)
    i.show()
    time.sleep(2)
  def bark(self):
    self.sound('barks.wav')
  def whimper(self):
    self.sound('whimpers.wav')
  def sniff(self):
    self.sound('sniffs.wav')
  def eat_cake(self):
    self.image('cake'+ str(rint(1,4)) + '.png')
  def jump_hoop(self):
    self.image('hoop'+ str(rint(1,4)) + '.png')
  def swim(self):
    self.image('swim' + str(rint(1,4)) + '.png')
  def sleep(self):
    self.image('sleep' + str(rint(1,4)) + '.png')

