from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
from quick_resto_objects.modules.crm.fixed_discount import convert_str_to_type_discount, TypeDiscount
from quick_resto_objects.modules.crm.markup import Day, TimeRange
from quick_resto_objects.modules.warehouse.dish import Dish
from quick_resto_objects.modules.warehouse.dish_category import DishCategory
from quick_resto_objects.modules.warehouse.modifier_group import ModifierGroup
from quick_resto_objects.modules.warehouse.sale_place import SalePlace
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

    def __init__(self, name: str = None, deleted: bool = None, typeDiscount: str = None, value: float = None,
                 categories: set = None, dishes: set = None,
                 tags: set = None, modifierGroups: list = None, salePlaces: set = None, dateRange: dict = None,
                 days: list = None,
                 operatorCancellable: bool = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.scheduled.ScheduledDiscount"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._deleted: bool = deleted
        self._type_discount = convert_str_to_type_discount(typeDiscount)

        if dateRange is not None: 
            self._date_range = TimeRange(**dateRange)
        else:
            self._date_range = None

        self._operator_cancellable = operatorCancellable
        self._value: float = value

        if categories is not None: 
            self._categories: set = [DishCategory(**category) for category in categories]
        else:
            self._categories = None

        if dishes is not None:
            self._dishes: set = [Dish(**dish) for dish in dishes]
        else:
            self._dishes = None

        if tags is not None:
            self._tags: set = [StoreItemTag(**value) for value in tags]
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

        if days is not None: 
            self._days: list = [Day(**day) for day in days]
        else:
            self._days = None
