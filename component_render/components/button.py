from .label import Label
from .icon import Icon
from .base_component import BaseComponent
from ..actions.action import ClickAction


class Button(BaseComponent):
    def __init__(self):
        super().__init__()
        self._label = None
        self._variant = None
        self._size = None
        self._iconRight = None
        self._disabled = None
        self._clickAction = None

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value: Label):
        self._label = value

    @property
    def variant(self):
        return self._variant

    @variant.setter
    def variant(self, value: str):
        self._variant = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: str):
        self._size = value

    @property
    def iconRight(self):
        return self._iconRight

    @iconRight.setter
    def iconRight(self, value: Icon):
        self._iconRight = value

    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value: bool):
        self._disabled = value

    @property
    def clickAction(self):
        return self._clickAction

    @clickAction.setter
    def clickAction(self, value: ClickAction):
        self._clickAction = value 