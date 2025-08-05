from ..components.color import Color
from ..components.base_component import BaseComponent


class SeparatorSnippet(BaseComponent):
    def __init__(self):
        super().__init__()
        self.thickness = None
        self.marginVertical = None
        self.color = None
    
    def set_thickness(self, thickness: int):
        self.thickness = thickness
        return self
    
    def set_margin_vertical(self, marginVertical: int):
        self.marginVertical = marginVertical
        return self
    
    def set_color(self, color: Color):
        self.color = color
        return self 