from typing import Optional, Dict, Any
from .base_click_action import BaseClickAction


class OpenBottomSheetAction(BaseClickAction):
    def __init__(
        self,
        type: str,
        data: Optional[Dict[str, Any]] = None
    ):
        super().__init__(type='OPEN_BOTTOMSHEET', data=data)
        self.bottomSheetType = type
        self.bottomSheetData = data 