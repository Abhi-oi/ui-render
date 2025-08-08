from typing import Optional
from ..properties.color_type import ColorType
from .label import Label
from .base_component import BaseComponent


class Tag(BaseComponent):
    def __init__(self):
        super().__init__()
        self._label = None
        self._bgColor = None 
        self._borderRadius = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value: Label):
        self._label = value

    @property
    def bgColor(self):
        return self._bgColor

    @bgColor.setter
    def bgColor(self, value: ColorType):
        self._bgColor = value

    @property
    def borderRadius(self):
        return self._borderRadius

    @borderRadius.setter
    def borderRadius(self, value: int):
        self._borderRadius = value 