from .bottom_sheet import BottomSheet
from .title import Title
from .subtitle import Subtitle
from .icon import Icon


class BottomSheetHeader(BottomSheet):
    def __init__(self):
        super().__init__("BottomSheetHeader")
        self.title = None
        self.subtitle = None
        self.icon = None
    
    def set_title(self, title: Title):
        self.title = title
        return self
    
    def set_subtitle(self, subtitle: Subtitle):
        self.subtitle = subtitle
        return self
    
    def set_icon(self, icon: Icon):
        self.icon = icon
        return self 