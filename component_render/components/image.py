from typing import Optional
from .base_component import BaseComponent


class Image(BaseComponent):
    def __init__(self, src: str):
        super().__init__()
        self.src = src
        self.width = None
        self.height = None
        self.aspectRatio = None
        self.containerShape = None
    
    def set_width(self, width: int):
        self.width = width
        return self
    
    def set_height(self, height: int):
        self.height = height
        return self
    
    def set_aspect_ratio(self, aspectRatio: float):
        self.aspectRatio = aspectRatio
        return self
    
    def set_container_shape(self, containerShape: str):
        self.containerShape = containerShape
        return self 