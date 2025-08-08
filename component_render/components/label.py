from typing import Optional
from ..properties.font import Font
from ..properties.weight import Weight
from ..properties.size import Size
from .base_component import BaseComponent
from .constant import TextAlign

class Label(BaseComponent):
    def __init__(self, text: str):
        super().__init__()
        self._text = text
        self._font = None
        self._color = None
        self._textAlign = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value: Font):
        self._font = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def textAlign(self):
        return self._textAlign

    @textAlign.setter
    def textAlign(self, value: TextAlign):
        self._textAlign = value 







