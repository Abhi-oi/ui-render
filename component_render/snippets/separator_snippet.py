from ..properties.color_type import ColorType
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType


class SeparatorSnippet(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.SEPARATOR_SNIPPET.value, data={})
        self._thickness = None
        self._marginVertical = None
        self._color = None

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value: int):
        self._thickness = value
        self._data['thickness'] = value

    @property
    def marginVertical(self):
        return self._marginVertical

    @marginVertical.setter
    def marginVertical(self, value: int):
        self._marginVertical = value
        self._data['marginVertical'] = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: ColorType):
        self._color = value
        self._data['color'] = value.value if value else None 