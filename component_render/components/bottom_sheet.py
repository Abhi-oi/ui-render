from typing import Dict, Any
from .base_component import BaseComponent


class BottomSheet(BaseComponent):
    def __init__(self, type: str):
        super().__init__()
        self.type = type
        self.data = None
    
    def set_data(self, data: Dict[str, Any]):
        self.data = data
        return self 