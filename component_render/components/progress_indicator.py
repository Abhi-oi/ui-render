from .title import Title
from .subtitle import Subtitle
from .color import Color
from .base_component import BaseComponent


class ProgressIndicator(BaseComponent):
    def __init__(self, percentage: int):
        super().__init__()
        self.percentage = percentage
        self.size = None
        self.strokeWidth = None
        self.title = None
        self.subtitle = None
        self.bgColor = None
        self.progressColor = None
        self.showPercentage = None
        self.animated = None
    
    def set_size(self, size: int):
        self.size = size
        return self
    
    def set_stroke_width(self, strokeWidth: int):
        self.strokeWidth = strokeWidth
        return self
    
    def set_title(self, title: Title):
        self.title = title
        return self
    
    def set_subtitle(self, subtitle: Subtitle):
        self.subtitle = subtitle
        return self
    
    def set_bg_color(self, bgColor: Color):
        self.bgColor = bgColor
        return self
    
    def set_progress_color(self, progressColor: Color):
        self.progressColor = progressColor
        return self
    
    def set_show_percentage(self, showPercentage: bool):
        self.showPercentage = showPercentage
        return self
    
    def set_animated(self, animated: bool):
        self.animated = animated
        return self 