from keyboard import Keyboard
from mouse import Mouse


class Action:
    def __init__(self) -> None:
        self.mouse = Mouse()
        self.keyboard = Keyboard()

    def cast():
        pass

    def hook(self):
        self.mouse.click_left_mouse_key()

    def enter_fishing(self):
        self.keyboard.press_key('F3')

    def cast(self, delay_in_milli):
        self.mouse.click_left_mouse_key(delay_in_milli=1000)
