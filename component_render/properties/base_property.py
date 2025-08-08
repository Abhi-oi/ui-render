


class BaseProperty():
    def _todict(self):
        result = {}
        for key, value in self.__dict__.items():
            print(key, value)
            key = key.replace('_', '')
            if value is not None:
                if hasattr(value, 'to_dict'):
                    result[key] = value.to_dict()
                elif isinstance(value, list):
                    result[key] = [item.to_dict() if hasattr(item, 'to_dict') else item for item in value]
                elif hasattr(value, 'value'): 
                    result[key] = value.value
                else:
                    result[key] = value
        return result

    def to_dict(self):
        return self._todict()
