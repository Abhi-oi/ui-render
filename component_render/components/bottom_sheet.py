from typing import Dict, Any
from .base_component import BaseComponent


class BottomSheet(BaseComponent):
    def __init__(self, type: str):
        super().__init__()
        self._type = type
        self._data = None

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: Dict[str, Any]):
        self._data = value 