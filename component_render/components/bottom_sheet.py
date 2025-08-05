from typing import Dict, Any


class BottomSheet:
    def __init__(self, type: str):
        self.type = type
        self.data = None
    
    def set_data(self, data: Dict[str, Any]):
        self.data = data
        return self 