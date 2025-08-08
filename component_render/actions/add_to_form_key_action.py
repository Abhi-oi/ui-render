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
        self._position = position
        self._formKey = formKey
        self._content = content

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: str):
        self._position = value

    @property
    def formKey(self):
        return self._formKey

    @formKey.setter
    def formKey(self, value: str):
        self._formKey = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value: Dict[str, Any]):
        self._content = value 