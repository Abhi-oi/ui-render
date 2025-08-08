from ..components.label import Label
from ..components.icon import Icon
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class BottomSheetHeaderSnippet(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.BOTTOM_SHEET_HEADER_SNIPPET.value, data={})
        self._title = None
        self._subtitle = None
        self._icon = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: Label):
        self._title = value
        self._data['title'] = value

    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value: Label):
        self._subtitle = value
        self._data['subtitle'] = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value: Icon):
        self._icon = value
        self._data['icon'] = value 