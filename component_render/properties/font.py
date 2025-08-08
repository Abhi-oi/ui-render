from .weight import Weight
from .size import Size
from .base_property import BaseProperty

class Font(BaseProperty):
    def __init__(self, weight: Weight = None, size: Size = None):
        self._weight = weight
        self._size = size

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value: Weight):
        self._weight = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: Size):
        self.size=value