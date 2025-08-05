from ..components.card import Card
from ..components.icon import Icon
from ..components.label import Label
from ..components.base_component import BaseComponent


class InfoSnippetType3(BaseComponent):
    def __init__(self):
        super().__init__()
        self.card = None
        self.icon = None
        self.title = None
    
    def set_card(self, card: Card):
        self.card = card
        return self
    
    def set_icon(self, icon: Icon):
        self.icon = icon
        return self
    
    def set_title(self, title: Label):
        self.title = title
        return self 