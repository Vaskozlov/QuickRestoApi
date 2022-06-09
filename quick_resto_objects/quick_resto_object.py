import json
from enum import Enum


class QuickRestoObject(object):
    @property
    def object_id(self) -> int:
        return self._object_id

    @property
    def global_id(self) -> int:
        return self._global_id

    @property
    def class_name(self) -> str:
        return self._class_name

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return json.dumps(self, cls=QuickRestoObjectEncoder, indent=4, ensure_ascii=False)

    def __init__(self, id: int, className: str, _id: int = 0, **kwargs):
        self._object_id: int = id
        self._global_id: int = _id
        self._class_name: str = className


class QuickRestoObjectEncoder(json.JSONEncoder):
    def default(self, obj):

        if isinstance(obj, QuickRestoObject):
            return obj.__dict__
        elif isinstance(obj, Enum):
            return obj.value

        return json.JSONEncoder.default(self, obj)
