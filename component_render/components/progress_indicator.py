from .label import Label
from ..properties.color_type import ColorType
from .base_component import BaseComponent


class ProgressIndicator(BaseComponent):
    def __init__(self, percentage: int):
        super().__init__()
        self._percentage = percentage
        self._size = None
        self._strokeWidth = None
        self._title = None
        self._subtitle = None
        self._bgColor = None  # Should be ColorType
        self._progressColor = None  # Should be ColorType
        self._showPercentage = None
        self._animated = None

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value: int):
        self._percentage = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        self._size = value

    @property
    def strokeWidth(self):
        return self._strokeWidth

    @strokeWidth.setter
    def strokeWidth(self, value: int):
        self._strokeWidth = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: Label):
        self._title = value

    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value: Label):
        self._subtitle = value

    @property
    def bgColor(self):
        return self._bgColor

    @bgColor.setter
    def bgColor(self, value: ColorType):
        self._bgColor = value

    @property
    def progressColor(self):
        return self._progressColor

    @progressColor.setter
    def progressColor(self, value: ColorType):
        self._progressColor = value

    @property
    def showPercentage(self):
        return self._showPercentage

    @showPercentage.setter
    def showPercentage(self, value: bool):
        self._showPercentage = value

    @property
    def animated(self):
        return self._animated

    @animated.setter
    def animated(self, value: bool):
        self._animated = value 