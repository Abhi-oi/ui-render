from ..components.card import Card
from ..components.label import Label
from ..components.icon import Icon
from ..actions.action import ClickAction
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class InfoSnippetType3(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.INFO_SNIPPET_TYPE_3.value, data={})
        self._card = None
        self._icon = None
        self._title = None
        self._clickAction = None

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value: Card):
        self._card = value
        self._data['card'] = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value: Icon):
        self._icon = value
        self._data['icon'] = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: Label):
        self._title = value
        self._data['title'] = value

    @property
    def clickAction(self):
        return self._clickAction

    @clickAction.setter
    def clickAction(self, value: ClickAction):
        self._clickAction = value
        self._data['clickAction'] = value 