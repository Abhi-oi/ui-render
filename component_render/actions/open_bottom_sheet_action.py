from typing import Optional, Dict, Any
from .base_click_action import BaseClickAction


class OpenBottomSheetAction(BaseClickAction):
    def __init__(
        self,
        type: str,
        data: Optional[Dict[str, Any]] = None
    ):
        super().__init__(type='OPEN_BOTTOMSHEET', data=data)
        self._bottomSheetType = type
        self._bottomSheetData = data

    @property
    def bottomSheetType(self):
        return self._bottomSheetType

    @bottomSheetType.setter
    def bottomSheetType(self, value: str):
        self._bottomSheetType = value

    @property
    def bottomSheetData(self):
        return self._bottomSheetData

    @bottomSheetData.setter
    def bottomSheetData(self, value: Optional[Dict[str, Any]]):
        self._bottomSheetData = value 