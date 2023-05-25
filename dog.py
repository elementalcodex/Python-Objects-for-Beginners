import sys
import time
from IPython.display import Audio, display

#d = '/content/Python-Objects-for-Beginners/'
#sys.path.insert(0, d )

class Dog:
  def bark(self):
    display(Audio('barks.wav', autoplay=True))
    time.sleep(2)
