from .bottom_sheet import BottomSheet
from .button import Button


class BottomSheetFooter(BottomSheet):
    def __init__(self):
        super().__init__("BottomSheetFooter")
        self.primaryButton = None
        self.secondaryButton = None
    
    def set_primary_button(self, primaryButton: Button):
        self.primaryButton = primaryButton
        return self
    
    def set_secondary_button(self, secondaryButton: Button):
        self.secondaryButton = secondaryButton
        return self 