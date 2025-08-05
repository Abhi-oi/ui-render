from ..components.label import Label
from ..components.base_component import BaseComponent


class SectionHeaderSnippet(BaseComponent):
    def __init__(self):
        super().__init__()
        self.title = None
        self.subtitle = None
    
    def set_title(self, title: Label):
        self.title = title
        return self
    
    def set_subtitle(self, subtitle: Label):
        self.subtitle = subtitle
        return self 