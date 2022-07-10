from enum import Enum

from quick_resto_objects.modules.warehouse.dish import Dish
from quick_resto_objects.modules.warehouse.dish_category import DishCategory
from quick_resto_objects.modules.warehouse.modifier_group import ModifierGroup
from quick_resto_objects.modules.warehouse.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class TypeDiscount(Enum):
    ABSOLUTE = "ABSOLUTE"
    PERCENT = "PERCENT"
    NONE = "NONE"


StrToTypeDiscount = {
    TypeDiscount.ABSOLUTE.value: TypeDiscount.ABSOLUTE,
    TypeDiscount.PERCENT.value: TypeDiscount.PERCENT,
}


def convert_str_to_type_discount(value: str) -> TypeDiscount:
    if value in TypeDiscount.keys():
        return TypeDiscount[value]

    return TypeDiscount.NONE


class FixedDiscount(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def type_discount(self) -> TypeDiscount:
        return self._type_discount

    @property
    def value(self) -> float:
        return self._value

    @property
    def categories(self) -> set:
        return self._categories

    @property
    def dishes(self) -> set:
        return self._dishes

    @property
    def tags(self) -> set:
        return self._tags

    @property
    def modifier_groups(self) -> list:
        return self._modifier_groups

    @property
    def sale_places(self) -> set:
        return self._sale_places

    @property
    def index(self) -> int:
        return self._index

    def __init__(self, name: str = None, deleted: bool = None, typeDiscount: str = None, value: float = None,
                 categories: set = None, dishes: set = None,
                 tags: set = None, modifierGroups: list = None, salePlaces: set = None, index: int = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.fixed.FixedDiscount"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._deleted: bool = deleted
        self._type_discount = convert_str_to_type_discount(typeDiscount)
        self._value: float = value

        if categories is not None: 
            self._categories: set = [DishCategory(**category) for category in categories]
        else:
            self._categories = None

        if dishes is not None: 
            self._dishes: set = [Dish(**dish) for dish in dishes]
        else:
            self._dishes

        if tags is not None: 
            self._tags: set = tags
        else:
            self._tags = None

        if modifierGroups is not None: 
            self._modifier_groups: list = [ModifierGroup(**group) for group in modifierGroups]
        else:
            self._modifier_groups = None

        if salePlaces is not None: 
            self._sale_places: set = [SalePlace(**place) for place in salePlaces]
        else:
            self._sale_places = None

        self._index: int = index
