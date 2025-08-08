from ..components.label import Label
from ..components.progress_indicator import ProgressIndicator
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class InfoSnippetType2(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.INFO_SNIPPET_TYPE_2.value, data={})
        self._title = None
        self._subtitle = None
        self._progressIndicator = None

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
    def progressIndicator(self):
        return self._progressIndicator

    @progressIndicator.setter
    def progressIndicator(self, value: ProgressIndicator):
        self._progressIndicator = value
        self._data['progressIndicator'] = value 