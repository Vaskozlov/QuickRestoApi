from quick_resto_objects.modules.core.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
from quick_resto_objects.modules.warehouse.dish_sale import DishSale
from quick_resto_objects.quick_resto_object import QuickRestoObject


class Modifier(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def article(self) -> int:
        return self._article

    @property
    def with_dish(self) -> bool:
        return self._with_dish

    @property
    def measure_unit(self) -> MeasureUnit:
        return self._measure_unit

    @property
    def title_in_price(self) -> str:
        return self._titleInPrice

    @property
    def item_title(self) -> bool:
        return self._item_title

    @property
    def min_value(self) -> int:
        return self._min_value

    @property
    def max_value(self) -> int:
        return self._max_value

    @property
    def modifier_sales(self) -> list:
        return self._modifier_sales

    @property
    def exclude_discount(self) -> bool:
        return self._exclude_discount

    @property
    def exclude_markup(self) -> bool:
        return self._exclude_markup

    @property
    def store_quantity_kg(self) -> float:
        return self._store_quantity_kg

    @property
    def default_value(self) -> int:
        return self._default_value

    @property
    def minimal_price(self) -> float:
        return self._minimal_price

    @property
    def base_price_in_list(self) -> float:
        return self._base_price_in_list

    @property
    def pack(self) -> float:
        return self._pack

    @property
    def recipe(self) -> str:
        return self._recipe

    @property
    def price(self) -> float:
        return self._price

    @property
    def store_item_tag(self) -> StoreItemTag:
        return self._store_item_tag

    def __init__(self, name: str = None, measureUnit: dict = None, color: str = None, displayOnTerminal: bool = None,
                 minValue: int = None, maxValue: int = None, withDish: bool = None,
                 modifierSales: list = None, excludeDiscount: bool = None, excludeMarkup: bool = None,
                 article: int = None, itemTitle: str = None,
                 titleInPrice: str = None, storeQuantityKg: float = None, defaultValue: int = None,
                 basePriceInList: float = None, pack: float = None, recipe: str = None,
                 price: float = None, minimalPrice: float = None, deleted: bool = None, storeItemTag=None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.mods.ModifierGroup"

        super().__init__(class_name=class_name, **kwargs)

        self._name = name
        self._deleted = deleted
        self._measure_unit = measureUnit
        self._color = color
        self._display_on_terminal = displayOnTerminal
        self._min_value = minValue
        self._max_value = maxValue
        self._with_dish = withDish

        if modifierSales is not None:
            self._modifier_sales: list = [DishSale(**dish_sale) for dish_sale in modifierSales]
        else:
            self._modifier_sales = None

        self._item_title = itemTitle
        self._article = article
        self._titleInPrice = titleInPrice
        self._exclude_discount = excludeDiscount
        self._exclude_markup = excludeMarkup
        self._store_quantity_kg = storeQuantityKg
        self._default_value = defaultValue
        self._minimal_price = minimalPrice
        self._base_price_in_list = basePriceInList
        self._pack = pack
        self._recipe = recipe
        self._price = price

        if storeItemTag is not None:
            self._store_item_tag = StoreItemTag(**storeItemTag)
        else:
            self._store_item_tag = None
