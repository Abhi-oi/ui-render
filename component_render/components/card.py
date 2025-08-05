from typing import Optional
from .color import Color


class Card:
    def __init__(self):
        self.bgColor = None
        self.borderColor = None
    
    def set_bg_color(self, bgColor: Color):
        self.bgColor = bgColor
        return self
    
    def set_border_color(self, borderColor: Color):
        self.borderColor = borderColor
        return self 