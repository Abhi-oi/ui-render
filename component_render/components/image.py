from typing import Optional
from .base_component import BaseComponent

from .constant import ContainerShape

class Image(BaseComponent):
    def __init__(self, src: str):
        super().__init__()
        self._src = src
        self._width = None
        self._height = None
        self._aspectRatio = None
        self._containerShape = None

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value: str):
        self._src = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value

    @property
    def aspectRatio(self):
        return self._aspectRatio

    @aspectRatio.setter
    def aspectRatio(self, value: float):
        self._aspectRatio = value

    @property
    def containerShape(self):
        return self._containerShape

    @containerShape.setter
    def containerShape(self, value: ContainerShape):
        self._containerShape = value 