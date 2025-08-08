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
        self._endpoint = endpoint
        self._method = method
        self._requestBody = requestBody or {}

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value: str):
        self._endpoint = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value: str):
        self._method = value

    @property
    def requestBody(self):
        return self._requestBody

    @requestBody.setter
    def requestBody(self, value: Optional[Dict[str, Any]]):
        self._requestBody = value 