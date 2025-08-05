from typing import Optional, Dict, Any
from .base_click_action import BaseClickAction


class NavigateAction(BaseClickAction):
    def __init__(
        self,
        screen: str,
        params: Optional[Dict[str, Any]] = None
    ):
        data = {
            'screen': screen,
            'params': params or {}
        }
        super().__init__(type='NAVIGATE', data=data)
        self.screen = screen
        self.params = params or {} 