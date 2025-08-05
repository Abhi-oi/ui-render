from ..components.button import Button
from ..components.base_component import BaseComponent


class BottomSheetFooterSnippet(BaseComponent):
    def __init__(self):
        super().__init__()
        self.primaryButton = None
        self.secondaryButton = None
    
    def set_primary_button(self, primaryButton: Button):
        self.primaryButton = primaryButton
        return self
    
    def set_secondary_button(self, secondaryButton: Button):
        self.secondaryButton = secondaryButton
        return self 