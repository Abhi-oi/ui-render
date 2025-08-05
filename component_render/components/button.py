from .label import Label
from .icon import Icon
from .base_component import BaseComponent
from ..actions.action import ClickAction


class Button(BaseComponent):
    def __init__(self):
        super().__init__()
        self.label = None
        self.variant = None
        self.size = None
        self.iconRight = None
        self.disabled = None
        self.clickAction = None
    
    def set_label(self, label: Label):
        self.label = label
        return self
    
    def set_variant(self, variant: str):
        self.variant = variant
        return self
    
    def set_size(self, size: str):
        self.size = size
        return self
    
    def set_icon_right(self, iconRight: Icon):
        self.iconRight = iconRight
        return self
    
    def set_disabled(self, disabled: bool):
        self.disabled = disabled
        return self
    
    def set_click_action(self, clickAction: ClickAction):
        self.clickAction = clickAction
        return self 