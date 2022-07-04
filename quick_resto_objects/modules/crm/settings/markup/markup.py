from quick_resto_objects.modules.core.dictionaries.storeitemtag.store_item_tag import StoreItemTag
from quick_resto_objects.modules.crm.settings.fixed.fixed_discount import TypeDiscount, convert_str_to_type_discount
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish import Dish
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish_category import DishCategory
from quick_resto_objects.modules.warehouse.nomenclature.mods.modifier_group import ModifierGroup
from quick_resto_objects.modules.warehouse.nomenclature.sale_place.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject

class TimeRange:
    @property
    def start(self) -> str:
        return self._start

    @property
    def end(self) -> str:
        return self._end

    def __init__(self, start: str, end: str):
        self._start: str = start
        self._end: str = end

class Day(QuickRestoObject):
    @property
    def day(self) -> str:
        return self._day

    @property
    def active(self) -> bool:
        return self._active

    @property
    def time_range(self) -> TimeRange:
        return self._time_range

    def __init__(self, day: str, active: bool, timeRange: dict, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.markup.Day"
        super().__init__(class_name=class_name, **kwargs)

        self._day: str = day
        self._active: bool = active
        self._time_range: dict = TimeRange(**timeRange)

class Markup(QuickRestoObject):
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
    def operator_cancellable(self) -> bool:
        return self._operator_cancellable

    @property
    def date_range(self) -> TimeRange:
        return self._date_range

    @property
    def categories(self) -> list:
        return self._categories

    @property
    def dishes(self) -> list:
        return self._dishes

    @property
    def tags(self) -> list:
        return self._tags

    @property
    def modifier_groups(self) -> list:
        return self._modifier_groups

    @property
    def sale_places(self) -> list:
        return self._sale_places

    @property
    def days(self) -> list:
        return self._days

    def __init__(self, name: str, deleted: bool, typeDiscount: str, value: float, operatorCancellable: bool, 
                dateRange: dict, categories: list, dishes: list, tags: list, modifierGroups: list, salePlaces: list, 
                days: list, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.markup.Markup"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._deleted: bool = deleted
        self._type_discount: str = convert_str_to_type_discount(typeDiscount)
        self._value: float = value
        self._operator_cancellable: bool = operatorCancellable
        self._date_range: dict = TimeRange(**dateRange)
        self._categories: list = [DishCategory(**category) for category in categories]
        self._dishes: list = [Dish(**dish) for dish in dishes]
        self._tags: list = [StoreItemTag(**tag) for tag in tags]
        self._modifier_groups: list = [ModifierGroup(**group) for group in categories]
        self._sale_places: list = [SalePlace(**place) for place in salePlaces]
        self._days: list = [Day(**day) for day in days]