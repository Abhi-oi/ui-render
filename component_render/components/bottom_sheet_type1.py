from .bottom_sheet import BottomSheet


class BottomSheetType1(BottomSheet):
    def __init__(self):
        super().__init__("BottomSheetType1")
        self._header = None
        self._items = []
        self._footer = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value: list):
        self._items = value

    @property
    def footer(self):
        return self._footer

    @footer.setter
    def footer(self, value):
        self._footer = value 