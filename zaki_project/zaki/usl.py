import os
import time
import sys

def typewriter(text):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    if text != "\n":
      time.sleep(0.1)
    else:
      time.sleep(1)