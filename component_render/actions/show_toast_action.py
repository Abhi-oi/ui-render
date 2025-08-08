from typing import Optional, Dict, Any
from .base_click_action import BaseClickAction


class ShowToastAction(BaseClickAction):
    def __init__(
        self,
        message: str,
        variant: str,
        successAction: Optional[Dict[str, Any]] = None
    ):
        data = {
            'message': message,
            'variant': variant,
            'successAction': successAction
        }
        super().__init__(type='SHOW_TOAST', data=data)
        self._message = message
        self._variant = variant
        self._successAction = successAction

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value: str):
        self._message = value

    @property
    def variant(self):
        return self._variant

    @variant.setter
    def variant(self, value: str):
        self._variant = value

    @property
    def successAction(self):
        return self._successAction

    @successAction.setter
    def successAction(self, value: Optional[Dict[str, Any]]):
        self._successAction = value 