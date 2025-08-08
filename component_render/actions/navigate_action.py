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
        self._screen = screen
        self._params = params or {}

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, value: str):
        self._screen = value

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value: Optional[Dict[str, Any]]):
        self._params = value 