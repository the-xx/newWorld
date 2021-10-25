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


print("hello")
toplist, winlist = [], []




def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))


win32gui.EnumWindows(enum_cb, toplist)

new_world = [(hwnd, title)
             for hwnd, title in winlist if 'discord' in title.lower()]
# just grab the hwnd for first window matching firefox
new_world = new_world[0]
hwnd = new_world[0]
print(new_world)
box = win32gui.GetWindowRect(hwnd)
mon = {"top": box[1], "left": box[0], "width": box[2], "height": box[3]}
# mon = (0, 40, 800, 640)

sct = mss.mss()
win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)
print(bbox)
img = ImageGrab.grab(bbox)
# img.show()
last_time = time.time()

while True:



    img = np.asarray(sct.grab(mon))

    print("FPS: {}".format(1 / (time.time() - last_time)))
    last_time = time.time()
    # cv2.imshow('window', img)

    cv2.imshow('window', cv2.resize(img, (960, 540)))

    if cv2.waitKey(25) == ord('q'):
        cv2.destroyAllWindows()
        break




 