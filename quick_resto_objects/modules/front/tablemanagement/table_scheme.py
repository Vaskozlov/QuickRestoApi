from quick_resto_objects.modules.front.tablemanagement.hall.hall import Hall
from quick_resto_objects.modules.front.tablemanagement.table.table import Table
from quick_resto_objects.quick_resto_object import QuickRestoObject

class TableScheme(QuickRestoObject):
    @property
    def current_load(self) -> int:
        return self._current_load

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def title(self) -> str:
        return self._title

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @property
    def name(self) -> str:
        return self._name

    @property
    def reservations(self) -> list:
        return self._reservations

    @property
    def tables(self) -> list:
        return self._tables

    @property
    def halls(self) -> list:
        return self._halls

    def __init__(self, currentLoad: int, deleted: bool, width: int, height: int, itemTitle: str, maxCapacity: int,
                 name: str, tables: list, halls:list, reservations: list, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.tablemanagement.TableScheme"

        super().__init__(class_name=class_name, **kwargs)
        self._current_load: int = currentLoad
        self._deleted: bool = deleted
        self._width: int = width
        self._height: int = height
        self._title: str = itemTitle
        self._max_capacity: int = maxCapacity
        self._name: str = name
        self._reservations: list = reservations
        self._tables: list = [Table(**table) for table in tables]
        self._halls: list = [Hall(**value) for value in halls]
