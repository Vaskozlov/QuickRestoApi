from quick_resto_objects.modules.crm.settings.fixed.fixed_discount import TypeDiscount, convert_str_to_type_discount
from quick_resto_objects.modules.crm.settings.markup.markup import Day, TimeRange
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish import Dish
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish_category import DishCategory
from quick_resto_objects.modules.warehouse.nomenclature.mods.modifier_group import ModifierGroup
from quick_resto_objects.modules.warehouse.nomenclature.sale_place.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject

class ScheduledDiscount(QuickRestoObject):
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
    def date_range(self) -> TimeRange:
        return self._date_range

    @property
    def operator_cancellable(self) -> bool:
        return self._operator_cancellable

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
    def days(self) -> list:
        return self._days

    def __init__(self, name: str=None, deleted: bool=None, typeDiscount: str=None, value: float=None, categories: set=None, dishes: set=None, 
                    tags: set=None, modifierGroups: list=None, salePlaces: set=None, dateRange: dict=None, days: list=None,
                    operatorCancellable:bool=None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.scheduled.ScheduledDiscount"
        
        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._deleted: bool = deleted
        self._type_discount = convert_str_to_type_discount(typeDiscount)
        if (dateRange!=None):self._date_range = TimeRange(**dateRange)
        self._operator_cancellable = operatorCancellable
        self._value: float = value
        if (categories!=None):self._categories: set = [DishCategory(**category) for category in categories]
        self._dishes: set = [Dish(**dish) for dish in dishes]
        self._tags: set = tags
        if (modifierGroups!=None):self._modifier_groups: list = [ModifierGroup(**group) for group in modifierGroups]
        if (salePlaces!=None):self._sale_places: set = [SalePlace(**place) for place in salePlaces]
        if (days!=None):self._days: list = [Day(**day) for day in days]