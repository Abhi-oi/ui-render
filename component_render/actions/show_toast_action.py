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
        self.message = message
        self.variant = variant
        self.successAction = successAction 