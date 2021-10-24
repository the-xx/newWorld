import logging
import time
from abc import ABC, abstractmethod
import cv2

from context import PlayerContext

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class PlayerState(ABC):
    def __init__(self) -> None:
       _log.info("create " + self.__class__.__name__)

    @property
    def context(self) -> PlayerContext:
        return self._context

    @context.setter
    def context(self, context: PlayerContext) -> None:
        self._context = context


    @abstractmethod
    def do_something(self, context: PlayerContext):
        pass


class IdleState(PlayerState):


    def do_something(self, context: PlayerContext):
        cv2.imshow('window',context.image)

        if cv2.waitKey(25) == ord('q'):
            context.set_state(FISHING_STATE)
        else:
            context.set_state(IDLE_STATE)
        # while context.loop_time < 10000:
        #     context.loop_time += 1
        #     # cv2.waitKey(0)
        #     if cv2.waitKey(25) == ord('q'):
        #         context.set_state(FISHING_STATE)
        #     context.set_state(IDLE_STATE)
        # context.set_state(FISHING_STATE)



class FishingState(PlayerState):

    def do_something(self, context: PlayerContext):
        _log.info('finishing fishing')
        context._is_fish_on_hook = False
        context._halt = True
        cv2.destroyAllWindows()
        context.set_state(IDLE_STATE)

FISHING_STATE = FishingState()
IDLE_STATE = IdleState()
STATES= [FISHING_STATE, IDLE_STATE]