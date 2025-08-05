from .base_click_action import BaseClickAction


class CloseBottomSheetAction(BaseClickAction):
    def __init__(self):
        super().__init__(type='CLOSE_BOTTOMSHEET') 