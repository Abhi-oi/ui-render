from typing import Optional, Dict, Any
from .base_click_action import BaseClickAction


class ApiCallAction(BaseClickAction):
    def __init__(
        self,
        endpoint: str,
        method: str,
        requestBody: Optional[Dict[str, Any]] = None
    ):
        data = {
            'endpoint': endpoint,
            'method': method,
            'requestBody': requestBody or {}
        }
        super().__init__(type='API_CALL', data=data)
        self.endpoint = endpoint
        self.method = method
        self.requestBody = requestBody or {} 