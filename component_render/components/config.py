from ..properties.base_property import BaseProperty
from .constant import SnippetStacking

class Config(BaseProperty):
    def __init__(self):
        self._version = None
        self._snippetStacking = None
        self._viewportSize = None

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

    @property
    def snippetStacking(self):
        return self._snippetStacking

    @snippetStacking.setter
    def snippetStacking(self, value: SnippetStacking):
        self._snippetStacking = value

    @property
    def viewportSize(self):
        return self._viewportSize

    @viewportSize.setter
    def viewportSize(self, value: int):
        self._viewportSize = value 