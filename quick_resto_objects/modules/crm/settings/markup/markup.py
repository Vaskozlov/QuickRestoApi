from quick_resto_objects.modules.core.dictionaries.storeitemtag.store_item_tag import StoreItemTag
from quick_resto_objects.modules.crm.settings.fixed.fixed_discount import convert_str_to_type_discount, TypeDiscount
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

    def __init__(self, name: str = None, deleted: bool = None, typeDiscount: str = None, value: float = None,
                 operatorCancellable: bool = None,
                 dateRange: dict = None, categories: list = None, dishes: list = None, tags: list = None,
                 modifierGroups: list = None, salePlaces: list = None,
                 days: list = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.markup.Markup"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._deleted: bool = deleted
        self._type_discount = convert_str_to_type_discount(typeDiscount)
        self._value: float = value
        self._operator_cancellable: bool = operatorCancellable
        if (dateRange != None): self._date_range: dict = TimeRange(**dateRange)
        if (categories != None): self._categories: list = [DishCategory(**category) for category in categories]
        if (dishes != None): self._dishes: list = [Dish(**dish) for dish in dishes]
        if (tags != None): self._tags: list = [StoreItemTag(**tag) for tag in tags]
        if (modifierGroups != None): self._modifier_groups: list = [ModifierGroup(**group) for group in modifierGroups]
        if (salePlaces != None): self._sale_places: list = [SalePlace(**place) for place in salePlaces]
        if (days != None): self._days: list = [Day(**day) for day in days]
