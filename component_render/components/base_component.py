from ..actions.action import ClickAction


class BaseComponent:
    def __init__(self):
        self.clickAction = None
    
    def set_click_action(self, clickAction: ClickAction):
        self.clickAction = clickAction
        return self 