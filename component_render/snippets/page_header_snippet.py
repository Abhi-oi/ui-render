from ..components.label import Label
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class PageHeaderSnippet(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.PAGE_HEADER_SNIPPET.value, data={})
        self._title = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: Label):
        self._title = value
        self._data['title'] = value 