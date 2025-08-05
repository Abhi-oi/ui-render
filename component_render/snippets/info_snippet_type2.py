from ..components.label import Label
from ..components.progress_indicator import ProgressIndicator
from ..components.base_component import BaseComponent


class InfoSnippetType2(BaseComponent):
    def __init__(self):
        super().__init__()
        self.title = None
        self.subtitle = None
        self.progressIndicator = None
    
    def set_title(self, title: Label):
        self.title = title
        return self
    
    def set_subtitle(self, subtitle: Label):
        self.subtitle = subtitle
        return self
    
    def set_progress_indicator(self, progressIndicator: ProgressIndicator):
        self.progressIndicator = progressIndicator
        return self 