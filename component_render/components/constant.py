from enum import Enum

class SnippetStacking(Enum):
    VERTICAL = 'vertical'
    HORIZONTAL = 'horizontal' 

class TextAlign(Enum):
    LEFT = 'left'       
    CENTER = 'center'
    RIGHT = 'right'

class ContainerShape(Enum):
    ROUNDED = 'rounded'
    SQUARE = 'square'
    CIRCLE = 'circle'
