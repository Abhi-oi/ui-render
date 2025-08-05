from typing import Optional
from .label import Label
from .color import Color
from .base_component import BaseComponent


class Tag(BaseComponent):
    def __init__(self):
        super().__init__()
        self.label = None
        self.bgColor = None
        self.borderRadius = None
    
    def set_label(self, label: Label):
        self.label = label
        return self
    
    def set_bg_color(self, bgColor: Color):
        self.bgColor = bgColor
        return self
    
    def set_border_radius(self, borderRadius: int):
        self.borderRadius = borderRadius
        return self 