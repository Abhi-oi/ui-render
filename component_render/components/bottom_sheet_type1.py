from .bottom_sheet import BottomSheet


class BottomSheetType1(BottomSheet):
    def __init__(self):
        super().__init__("BottomSheetType1")
        self.header = None
        self.items = []
        self.footer = None
    
    def set_header(self, header):
        self.header = header
        return self
    
    def set_items(self, items: list):
        self.items = items
        return self
    
    def set_footer(self, footer):
        self.footer = footer
        return self 