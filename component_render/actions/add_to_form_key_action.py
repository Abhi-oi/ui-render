from typing import Optional, Dict, Any
from .base_click_action import BaseClickAction


class AddToFormKeyAction(BaseClickAction):
    def __init__(
        self,
        position: str,
        formKey: str,
        content: Dict[str, Any]
    ):
        data = {
            'position': position,
            'formKey': formKey,
            'content': content
        }
        super().__init__(type='ADD_TO_FORM_KEY', data=data)
        self.position = position
        self.formKey = formKey
        self.content = content 