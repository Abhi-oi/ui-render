from typing import List
from .base_click_action import BaseClickAction


class RefreshPagesAction(BaseClickAction):
    def __init__(
        self,
        pages: List[str]
    ):
        data = {
            'pages': pages
        }
        super().__init__(type='REFRESH_PAGES', data=data)
        self.pages = pages 