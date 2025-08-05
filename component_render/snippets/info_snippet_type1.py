from ..components.card import Card
from ..components.label import Label
from ..components.image import Image
from ..components.icon import Icon
from ..components.base_component import BaseComponent


class InfoSnippetType1(BaseComponent):
    def __init__(self):
        super().__init__()
        self.card = None
        self.title = None
        self.subtitle = None
        self.leftImage = None
        self.rightIcon = None
    
    def set_card(self, card: Card):
        self.card = card
        return self
    
    def set_title(self, title: Label):
        self.title = title
        return self
    
    def set_subtitle(self, subtitle: Label):
        self.subtitle = subtitle
        return self
    
    def set_left_image(self, leftImage: Image):
        self.leftImage = leftImage
        return self
    
    def set_right_icon(self, rightIcon: Icon):
        self.rightIcon = rightIcon
        return self
        