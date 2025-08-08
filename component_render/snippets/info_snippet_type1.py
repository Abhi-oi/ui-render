from ..components.card import Card
from ..components.label import Label
from ..components.image import Image
from ..components.icon import Icon
from ..actions.action import ClickAction
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class InfoSnippetType1(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.INFO_SNIPPET_TYPE_1.value, data={})
        self._card = None
        self._title = None
        self._subtitle = None
        self._leftImage = None
        self._rightIcon = None
        self._clickAction = None

    @property
    def card(self):
        return self._card

    @card.setter
    def card(self, value: Card):
        self._card = value
        self._data['card'] = value

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
    def leftImage(self):
        return self._leftImage

    @leftImage.setter
    def leftImage(self, value: Image):
        self._leftImage = value
        self._data['leftImage'] = value

    @property
    def rightIcon(self):
        return self._rightIcon

    @rightIcon.setter
    def rightIcon(self, value: Icon):
        self._rightIcon = value
        self._data['rightIcon'] = value

    @property
    def clickAction(self):
        return self._clickAction

    @clickAction.setter
    def clickAction(self, value: ClickAction):
        self._clickAction = value
        self._data['clickAction'] = value
