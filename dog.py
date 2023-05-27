import sys
import time
from IPython.display import Audio, display
from PIL import Image
from random import randint as rint

class Dog:
  def sound(self, sound_name):
    display(Audio('/content/Python-Objects-for-Beginners/dogsounds' + sound_name, autoplay=True))
    time.sleep(2)
  def image(self,img):
    i = Image.open('/content/Python-Objects-for-Beginners/dogpics' + img)
    i.show()
    time.sleep(2)
  def bark(self):
    self.sound('barks.wav')
  def whimper(self):
    self.sound('whimpers.wav')
  def sniff(self):
    self.sound('sniffs.wav')
  def eat_cake(self):
    self.image('cake'+ rint(1,4))
  def jump_hoop(self):
    self.image('hoop'+ rint(1,4))
  def swim(self):
    self.image('swim' + rint(1,4))
  def sleep(self):
    self.image('sleep' + rint(1,4))

