from ..components.label import Label
from ..components.icon import Icon
from ..components.base_component import BaseComponent


class BottomSheetHeaderSnippet(BaseComponent):
    def __init__(self):
        super().__init__()
        self.title = None
        self.subtitle = None
        self.icon = None
    
    def set_title(self, title: Label):
        self.title = title
        return self
    
    def set_subtitle(self, subtitle: Label):
        self.subtitle = subtitle
        return self
    
    def set_icon(self, icon: Icon):
        self.icon = icon
        return self 