import sys
import time
from IPython.display import Audio, display

class Dog:
  def bark(self):
    display(Audio('/content/Python-Objects-for-Beginners/barks.wav', autoplay=True))
    time.sleep(2)
print('woof')
