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
  def __sound__(self, sound_name):
    display(Audio('/content/Python-Objects-for-Beginners/dogsounds/' + sound_name, autoplay=True))
    time.sleep(2)
  def __image__(self,img):
    i = Image.open('/content/Python-Objects-for-Beginners/dogpics/' + img)
    i.show()
    time.sleep(2)
  def bark(self):
    self.__sound__('barks.wav')
  def whimper(self):
    self.__sound__('whimpers.wav')
  def sniff(self):
    self.__sound__('sniffs.wav')
  def eat_cake(self):
    self.__image__('cake'+ str(rint(1,4)) + '.png')
  def jump_hoop(self):
    self.__image__('hoop'+ str(rint(1,4)) + '.png')
  def swim(self):
    self.__image__('swim' + str(rint(1,4)) + '.png')
  def sleep(self):
    self.__image__('sleep' + str(rint(1,4)) + '.png')
  def __add__(self, add_num):
    self.health  += add_nun
  def __add__(self, add_num):
    self.health  = min(self.health + rint(0, add_num), 100)
    self.happiness  = min(self.happiness + rint(0, add_num), 100)
    self.energy  = min(self.energy + rint(0, add_nun), 100)
   
    
