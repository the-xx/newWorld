import win32api
import win32con
import time


class Mouse:
    def __init__(self) -> None:
        self.pressed_left = False
        self.pressed_right = False

    def press_left_mouse_key(self):
        if not self.pressed_left:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            self.pressed_left = True

    def release_left_mouse_key(self):
        if self.pressed_left:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            self.pressed_left = False

    def click_left_mouse_key(self, delay_in_milli=0.05, x=None, y=None):
        if x and y:
            win32api.SetCursorPos((x, y))
            time.sleep(0.02)
        self.press_left_mouse_key()
        time.sleep(delay_in_milli)
        self.release_left_mouse_key()

    def press_right_mouse_key(self):
        if not self.pressed_right:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
            self.pressed_right = True

    def release_right_mouse_key(self):
        if self.pressed_right:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
            self.pressed_right = False

    def click_right_mouse_key(self, delay_in_milli=0.05, x=None, y=None):
        if x and y:
            win32api.SetCursorPos((x, y))
            time.sleep(0.02)
        self.press_right_mouse_key()
        time.sleep(delay_in_milli)
        self.release_right_mouse_key()
