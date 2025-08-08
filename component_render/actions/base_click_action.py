from typing import Optional, Dict, Any
from ..properties.base_property import BaseProperty

class BaseClickAction(BaseProperty):
    def __init__(self, type: str, data: Optional[Dict[str, Any]] = None):
        self._type = type
        self._data = data

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
    def data(self, value: Optional[Dict[str, Any]]):
        self._data = value

    def to_dict(self):
        return self._todict() 