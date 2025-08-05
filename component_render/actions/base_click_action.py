from typing import Optional, Dict, Any


class BaseClickAction:
    def __init__(
        self,
        type: str,
        data: Optional[Dict[str, Any]] = None
    ):
        self.type = type
        self.data = data 