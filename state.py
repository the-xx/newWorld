import logging
import time
import numpy as np
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
        context.image = context.sct.grab(context.screen)

        cv2.imshow('window', np.array(context.image))

        if cv2.waitKey(25) == ord('q'):
            context.set_state(FISHING_STATE)
        else:
            context.set_state(IDLE_STATE)


class FishingState(PlayerState):

    def do_something(self, context: PlayerContext):
        _log.info('finishing fishing')
        context.is_fish_on_hook = False
        context.halt = True
        cv2.destroyAllWindows()
        context.set_state(IDLE_STATE)


FISHING_STATE = FishingState()
IDLE_STATE = IdleState()
STATES = [FISHING_STATE, IDLE_STATE]
