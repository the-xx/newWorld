from context import PlayerContext
from state import IDLE_STATE
import logging


context = PlayerContext()
context.set_state(IDLE_STATE)
# for i in range(8):

while not context.halt:
    context.step()
