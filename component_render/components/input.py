from typing import Optional
from .label import Label
from .base_component import BaseComponent


class Input(BaseComponent):
    def __init__(self):
        super().__init__()
        self.type = None
        self.placeholder = None
        self.value = None
        self.label = None
        self.required = None
        self.disabled = None
    
    def set_type(self, type: str):
        self.type = type
        return self
    
    def set_placeholder(self, placeholder: str):
        self.placeholder = placeholder
        return self
    
    def set_value(self, value: str):
        self.value = value
        return self
    
    def set_label(self, label: Label):
        self.label = label
        return self
    
    def set_required(self, required: bool):
        self.required = required
        return self
    
    def set_disabled(self, disabled: bool):
        self.disabled = disabled
        return self 