from ..components.label import Label
from ..components.base_component import BaseComponent


class PageHeaderSnippet(BaseComponent):
    def __init__(self):
        super().__init__()
        self.title = None
    
    def set_title(self, title: Label):
        self.title = title
        return self 