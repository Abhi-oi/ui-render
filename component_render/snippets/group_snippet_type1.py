from ..components.config import Config
from ..components.card import Card
from ..components.base_component import BaseComponent


class GroupSnippetType1(BaseComponent):
    def __init__(self):
        super().__init__()
        self.config = None
        self.card = None
        self.items = []
    
    def set_config(self, config: Config):
        self.config = config
        return self
    
    def set_card(self, card: Card):
        self.card = card
        return self
    
    def set_items(self, items: list):
        self.items = items
        return self 