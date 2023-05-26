import sys
import time
from IPython.display import Audio, display

class Dog:
  def __init__(self):
    d = '/content/Python-Objects-for-Beginners/'
    self.bark = d + 'barks.wav'
    self.sniff = d + 'sniffs.wav'
    self.whimper = d + 'whimpers.wav'
    
  def sound(self, sound_name):
    display(Audio(sound_name, autoplay=True))
    time.sleep(2)
  def bark(self):
    self.sound(self.bark)
  def whimper(self):
    self.sound(self.whimper)
  def sniff(self):
    self.sound(self.sniff)
