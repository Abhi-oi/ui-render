from .weight import Weight
from .size import Size


class Font:
    def __init__(self):
        self.weight = None
        self.size = None
    
    def set_weight(self, weight: Weight):
        self.weight = weight
        return self
    
    def set_size(self, size: Size):
        self.size = size
        return self 