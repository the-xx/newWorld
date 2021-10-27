
import logging
import sys
import cv2
from PIL import ImageGrab
import win32gui
import win32api
import numpy as np
import time
import mss

from action import Action


_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PlayerContext:
    _state = None
    is_fish_on_hook = False
    halt = False
    loop_time = 0
    image = None
    sct = mss.mss()  # move it out' ?
    bbox = None
    screen = None


    def __init__(self) -> None:
        _log.info("create new player context")

        self.mode = 'DEBUG'
        self.action = Action()
        # setup screen capture
        # left top right bottom
        self.bbox = self.__get_game_window_box()
        l = self.bbox[0]
        t = self.bbox[1]
        r = self.bbox[2]
        b = self.bbox[3]
        self.screen = {"top": t, "left": l, "width": r-l, "height": b-t}
        _log.info(self.screen)

    '''
    get coordinates for the game window
    '''
    def __get_game_window_box(self):
        def window_enumeration_handler(hwnd, top_windows):
            # Add window title and ID to array.
            top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

        top_windows = []
        win32gui.EnumWindows(window_enumeration_handler, top_windows)
        new_world_window_name = 'discord'
        new_world_windows = [(hwnd, title)
                             for hwnd, title in top_windows if new_world_window_name in title.lower()]
        # just grab the hwnd for first window matching game
        new_world_window = new_world_windows[0]
        hwnd = new_world_window[0]
        win32gui.SetForegroundWindow(hwnd)
        return win32gui.GetWindowRect(hwnd)

    def is_debug(self) -> bool:
        return self.mode == 'DEBUG'
    def set_state(self, state) -> None:
        _log.info(state)
        self._state = state

    def step(self):
        self._state.step(self)
