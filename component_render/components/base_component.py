from ..actions.action import ClickAction
from ..properties.base_property import BaseProperty

class BaseComponent(BaseProperty):
    def __init__(self):
        self._clickAction = None

    @property
    def clickAction(self):
        return self._clickAction

    @clickAction.setter
    def clickAction(self, value: ClickAction):
        self._clickAction = value

   
   