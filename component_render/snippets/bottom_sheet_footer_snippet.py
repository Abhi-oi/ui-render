from ..components.button import Button
from .base_snippet import BaseSnippet
from .snippet_type import SnippetType

class BottomSheetFooterSnippet(BaseSnippet):
    def __init__(self):
        super().__init__(type=SnippetType.BOTTOM_SHEET_FOOTER_SNIPPET.value, data={})
        self._primaryButton = None
        self._secondaryButton = None

    @property
    def primaryButton(self):
        return self._primaryButton

    @primaryButton.setter
    def primaryButton(self, value: Button):
        self._primaryButton = value
        self._data['primaryButton'] = value

    @property
    def secondaryButton(self):
        return self._secondaryButton

    @secondaryButton.setter
    def secondaryButton(self, value: Button):
        self._secondaryButton = value
        self._data['secondaryButton'] = value 