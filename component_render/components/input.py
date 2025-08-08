from typing import Optional
from .label import Label
from .base_component import BaseComponent


class Input(BaseComponent):
    def __init__(self):
        super().__init__()
        self._type = None
        self._placeholder = None
        self._value = None
        self._label = None
        self._required = None
        self._disabled = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def placeholder(self):
        return self._placeholder

    @placeholder.setter
    def placeholder(self, value: str):
        self._placeholder = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, value: Label):
        self._label = value

    @property
    def required(self):
        return self._required

    @required.setter
    def required(self, value: bool):
        self._required = value

    @property
    def disabled(self):
        return self._disabled

    @disabled.setter
    def disabled(self, value: bool):
        self._disabled = value