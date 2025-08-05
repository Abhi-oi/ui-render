from typing import Optional


class Color:
    def __init__(self):
        self.type = None
    
    def set_type(self, type: str):
        self.type = type
        return self 