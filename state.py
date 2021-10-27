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
    def step(self, context: PlayerContext):
        pass


class IdleState(PlayerState):

    def step(self, context: PlayerContext):
        context.image = context.sct.grab(context.screen)

        if context.is_debug():
            cv2.imshow('window', np.array(context.image))

        if cv2.waitKey(25) == ord('q'):
            context.set_state(FISHING_STATE)
        else:
            context.set_state(IDLE_STATE)

class FishingIdleState(PlayerState):
    def step(self, context: PlayerContext):
        # pull out the rod
        # action: f3
        context.set_state(CASTING_STATE)



class CastingState(PlayerState):
    def step(self, context: PlayerContext):
        # action: aim
        # action: release rod
        context.set_state(HOOKING_STATE)

class HookingState(PlayerState):
    def step(self, context: PlayerContext):
        context.image = context.sct.grab(context.screen)
        on_hook = False
        # sensor: on hook aka 'get ready'

        if on_hook:
            # action: click mouse
            context.set_state(REELING_STATE)
        else:
            context.set_state(HOOKING_STATE)
        pass

class ReelingState(PlayerState):
    def step(self, context: PlayerContext):
        context.image = context.sct.grab(context.screen)
        finish_reel = False
        # sensor: tension
        # sensor: finish reeling

        if finish_reel:
            context.set_state(IDLE_STATE)
        else:
            # action: hold mouse left / release mouse left
            context.set_state(REELING_STATE)


        pass

class FishingState(PlayerState):

    def step(self, context: PlayerContext):
        _log.info('finishing fishing')
        context.is_fish_on_hook = False
        context.halt = True
        if context.is_debug():
            cv2.destroyAllWindows()
        context.set_state(IDLE_STATE)

REELING_STATE = ReelingState()
HOOKING_STATE = HookingState()
FISHING_IDLE_STATE = FishingIdleState()
CASTING_STATE = CastingState()
FISHING_STATE = FishingState()
IDLE_STATE = IdleState()
STATES = [FISHING_STATE, IDLE_STATE]
