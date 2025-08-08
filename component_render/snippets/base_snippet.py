from ..components.base_component import BaseComponent

class BaseSnippet(BaseComponent):
    def __init__(self, type: str, data, config=None):
        super().__init__()
        self._type = type
        self._data = data
        self._config = config

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value