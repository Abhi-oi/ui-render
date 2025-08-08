from ..components.card import Card
from typing import List, Dict, Any
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class GroupSnippetType1(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.GROUP_SNIPPET_TYPE_1.value, data={})
        self._card = None
        self._items = []
        self._config = None

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value: Card):
        self._card = value
        self._data['card'] = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value: List[Dict[str, Any]]):
        self._items = value
        self._data['items'] = value

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value: Dict[str, Any]):
        self._config = value
        super().__setattr__('_config', value)