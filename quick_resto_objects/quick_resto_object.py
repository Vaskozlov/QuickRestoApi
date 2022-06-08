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

    def __init__(self, id: int, className: str, _id: int = 0, **kwargs):
        self._object_id: int = id
        self._global_id: int = _id
        self._class_name: str = className
