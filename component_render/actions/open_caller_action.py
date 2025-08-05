from .base_click_action import BaseClickAction


class OpenCallerAction(BaseClickAction):
    def __init__(self):
        super().__init__(type='OPEN_CALLER') 