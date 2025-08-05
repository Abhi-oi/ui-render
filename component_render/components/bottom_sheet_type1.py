from .bottom_sheet import BottomSheet
from .bottom_sheet_header import BottomSheetHeader
from .bottom_sheet_footer import BottomSheetFooter


class BottomSheetType1(BottomSheet):
    def __init__(self):
        super().__init__("BottomSheetType1")
        self.header = None
        self.items = []
        self.footer = None
    
    def set_header(self, header: BottomSheetHeader):
        self.header = header
        return self
    
    def set_items(self, items: list):
        self.items = items
        return self
    
    def set_footer(self, footer: BottomSheetFooter):
        self.footer = footer
        return self 