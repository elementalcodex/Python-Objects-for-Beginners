import sys
import time
from IPython.display import Audio, display

class Dog:
  def bark(self, sound):
    display(Audio(sound, autoplay=True))
    time.sleep(2)
print('woof')
