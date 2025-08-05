from typing import Optional
from .font import Font
from .color import Color
from .base_component import BaseComponent


class Label(BaseComponent):
    def __init__(self, text: str):
        super().__init__()
        self.text = text
        self.font = None
        self.color = None
        self.textAlign = None
    
    def set_font(self, font: Font):
        self.font = font
        return self
    
    def set_color(self, color: Color):
        self.color = color
        return self
    
    def set_text_align(self, textAlign: str):
        self.textAlign = textAlign
        return self 