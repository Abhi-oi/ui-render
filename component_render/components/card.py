from typing import Optional
from ..properties.color_type import ColorType
from .base_component import BaseComponent

class Card(BaseComponent):
    def __init__(self):
        super().__init__()
        self._bgColor = None 
        self._borderColor = None  

    @property
    def bgColor(self):
        return self._bgColor

    @bgColor.setter
    def bgColor(self, value: ColorType):
        self._bgColor = value

    @property
    def borderColor(self):
        return self._borderColor

    @borderColor.setter
    def borderColor(self, value: ColorType):
        self._borderColor = value 