from quick_resto_objects.quick_resto_object import QuickRestoObject


class TableScheme(QuickRestoObject):
    def __init__(self, currentLoad: int, deleted: bool, width: int, height: int, itemTitle: str, maxCapacity: int,
                 name: str,
                 reservations: list, **kwargs):
        class_name = "modules.front.tablemanagement.TableScheme"

        super().__init__(class_name=class_name, **kwargs)
        self._current_load: int = currentLoad
        self._deleted: bool = deleted
        self._width: int = width
        self._height: int = height
        self._title: str = itemTitle
        self._max_capacity: int = maxCapacity
        self._name: str = name
        self._reservations: list = reservations
