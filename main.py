from PIL import ImageGrab
import win32gui
import win32api
import cv2
import numpy as np
import time
import mss


'''
State:

fishing state:
* idle
* casting
* reeling
* reel finish

user state:


fishing action:
* enter fishing state
    * press F3
    * (optional): equip bait
* cast
    * aim
    * hold cast key
    * release when range indicator is at the top
* hook
    * detect `get ready`
    * press mouse left before time out
* reel
    * hold mouse left until red
    * release mouse left unitl green
    * finish when circle completes
* move if needed
* repair if needed



'''





 