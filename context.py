
import logging
import sys
import cv2


_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class PlayerContext:
    _state = None
    _is_fish_on_hook = False
    _halt = False
    loop_time = 0
    image = cv2.imread('D:\workspace\\newWorld\download.jpg')


    
    def __init__(self) -> None:
        _log.info("create new player context")
        

    def set_state(self, state) -> None:
        _log.info(state)
        self._state = state

 
    def do_something(self):
        self._state.do_something(self)
