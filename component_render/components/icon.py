from .base_component import BaseComponent
from ..actions.action import ClickAction


class Icon(BaseComponent):
    def __init__(self, name: str, size: str):
        super().__init__()
        self.name = name
        self.size = size
        self.clickAction = None
    
    def set_click_action(self, clickAction: ClickAction):
        self.clickAction = clickAction
        return self
