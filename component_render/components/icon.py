from .base_component import BaseComponent
from ..actions.action import ClickAction


class Icon(BaseComponent):
    def __init__(self, name: str, size: str):
        super().__init__()
        self._name = name
        self._size = size
        self._clickAction = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def clickAction(self):
        return self._clickAction

    @clickAction.setter
    def clickAction(self, value: ClickAction):
        self._clickAction = value
