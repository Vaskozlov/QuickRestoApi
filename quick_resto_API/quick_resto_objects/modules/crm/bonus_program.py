from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
from quick_resto_objects.modules.crm.account_type import AccountType
from quick_resto_objects.modules.crm.group import Group
from quick_resto_objects.modules.crm.markup import Day
from quick_resto_objects.modules.warehouse.dish import Dish
from quick_resto_objects.modules.warehouse.dish_category import DishCategory
from quick_resto_objects.quick_resto_object import QuickRestoObject

class BonusProgram(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def days(self) -> list:
        return self._days

    @property
    def groups(self) -> list:
        return self._groups

    @property
    def start_date(self) -> str:
        return self._start_date

    @property
    def end_date(self) -> str:
        return self._end_date

    @property
    def acc_value(self) -> float:
        return self._acc_value

    @property
    def account_type(self) -> AccountType:
        return self._account_type

    @property
    def do_not_accumulate_while_redeeming(self) -> bool:
        return self._do_not_accumulate_while_redeeming

    @property
    def greeting_bonus(self) -> float:
        return self._greeting_bonus

    @property
    def birthday_bonus(self) -> float:
        return self._birthday_bonus

    @property
    def categories(self) -> list:
        return self._categories

    @property
    def dishes(self) -> list:
        return self._dishes

    @property
    def tags(self) -> list:
        return self._tags

    def __init__(self, name: str = None, deleted: bool = None, days: list = None, groups: list = None,
                 startDate: str = None, endDate: str = None,
                 accValue: float = None, accountType: dict = None, doNotAccumulateWhileRedeeming: bool = None,
                 greetingBonus: float = None,
                 birthdayBonus: float = None, categories: list = None, dishes: list = None, tags: list = None,
                 **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.settings.bonus.BonusProgram"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._deleted: bool = deleted

        if days is not None: 
            self._days: list = [Day(**day) for day in days]
        else:
            self._days = None 

        if groups is not None: 
            self._groups: list = [Group(**group) for group in groups]
        else:
            self._groups = None

        self._start_date: str = startDate
        self._end_date: str = endDate
        self._acc_value: float = accValue

        if accountType is not None: 
            self._account_type: dict = AccountType(**accountType)
        else:
            self._account_type = None

        self._do_not_accumulate_while_redeeming: bool = doNotAccumulateWhileRedeeming
        self._greeting_bonus: float = greetingBonus
        self._birthday_bonus: float = birthdayBonus

        if categories is not None: 
            self._categories = [DishCategory(**category) for category in categories]
        else:
            self._categories = None

        if dishes is not None: 
            self._dishes: list = [Dish(**dish) for dish in dishes]
        else:
            self._dishes = None

        if tags is not None: 
            self._tags: list = [StoreItemTag(**tag) for tag in tags]
        else:
            self._tags = None
