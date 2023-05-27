import sys
import time
from IPython.display import Audio, display
from PIL import Image

class Dog:
  def sound(self, sound_name):
    display(Audio(sound_name, autoplay=True))
    time.sleep(2)
  def bark(self):
    self.sound('/content/Python-Objects-for-Beginners/barks.wav')
  def whimper(self):
    self.sound('/content/Python-Objects-for-Beginners/whimpers.wav')
  def sniff(self):
    self.sound('/content/Python-Objects-for-Beginners/sniffs.wav')
  def eat_cake(self):
    i = Image.open('/content/Python-Objects-for-Beginners/7.jpg')
    i.show()

