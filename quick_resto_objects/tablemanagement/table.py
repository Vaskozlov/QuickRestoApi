from enum import Enum
from quick_resto_objects.quick_resto_object import QuickRestoObject


class TableShape(Enum):
    RECT = 'RECT'
    NONE = 'NONE'


StrToTableShape = {
    TableShape.RECT.value: TableShape.RECT
}


def convert_str_to_selling_type(table_shape: str) -> TableShape:
    if table_shape in StrToTableShape.keys():
        return StrToTableShape[table_shape]

    return TableShape.NONE


class Table(QuickRestoObject):
    @property
    def angle(self) -> int:
        return self._angle

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def is_busy(self) -> bool:
        return self._is_busy

    @property
    def item_title(self) -> str:
        return self._item_title

    @property
    def min_capacity(self) -> int:
        return self._min_capacity

    @property
    def max_capacity(self) -> int:
        return self._max_capacity

    @property
    def reservable(self) -> bool:
        return self._reservable

    @property
    def shape(self) -> TableShape:
        return self._shape

    @property
    def title(self) -> str:
        return self._title

    def __init__(self, angle: int, deleted: bool, width: int, height: int, isBusy: bool, itemTitle: str,
                 minCapacity: int, maxCapacity: int, reservable: bool, shape: str, title: str, x: int, y: int,
                 **kwargs):
        super().__init__(className="modules.front.tablemanagement.Table", **kwargs)
        self._angle: int = angle
        self._deleted: bool = deleted
        self._x: int = x
        self._y: int = y
        self._width: int = width
        self._height: int = height
        self._is_busy: bool = isBusy
        self._item_title: str = itemTitle
        self._min_capacity: int = minCapacity
        self._max_capacity: int = maxCapacity
        self._reservable: bool = reservable
        self._title: str = title
        self._shape: TableShape = convert_str_to_selling_type(shape)
