from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.nomenclature.dish.dish_sales import DishSale
from quick_resto_objects.measureunits.measure_unit import MeasureUnit
from quick_resto_objects.nomenclature.dish.dish_category import convert_str_to_selling_type, SellingType


class Dish(QuickRestoObject):
    @property
    def article(self) -> int:
        return self._article

    @property
    def base_price_in_list(self) -> float:
        return self._base_price_in_list

    @property
    def dish_sales(self) -> list:
        return self._dish_sales

    @property
    def exclude_discount(self) -> int:
        return self._exclude_discount

    @property
    def display_on_terminal(self) -> bool:
        return self._display_on_terminal

    @property
    def exclude_markup(self) -> int:
        return self._exclude_markup

    @property
    def measure_unit(self) -> MeasureUnit:
        return self._measure_unit

    @property
    def minimal_price(self) -> float:
        return self._minimal_price

    @property
    def name(self) -> str:
        return self._name

    @property
    def pack(self) -> float:
        return self._pack

    @property
    def price(self) -> float:
        return self._price

    @property
    def ratio(self) -> float:
        return self._ratio

    @property
    def recipe(self) -> str:
        return self._recipe

    @property
    def selling_type(self) -> SellingType:
        return self._selling_type

    @property
    def store_quantity_kg(self) -> float:
        return self._store_quantity_kg

    def __init__(self, article: str, basePriceInList: float, dishSales: list, displayOnTerminal: bool,
                 excludeDiscount: bool, excludeMarkup: bool, measureUnit: dict, minimalPrice: float, name: str,
                 pack: float, price: float, ratio: float, recipe: str, sellingType: str, storeQuantityKg: float,
                 **kwargs):
        class_name: str = "modules.warehouse.nomenclature.Dish"

        super().__init__(class_name=class_name, **kwargs)
        self._article: int = int(article)
        self._base_price_in_list: float = basePriceInList
        self._dish_sales: list = [DishSale(**dish_sale) for dish_sale in dishSales]
        self._display_on_terminal: bool = displayOnTerminal
        self._exclude_discount: bool = excludeDiscount
        self._exclude_markup: bool = excludeMarkup
        self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        self._minimal_price: float = minimalPrice
        self._name: str = name
        self._pack: float = pack
        self._price: float = price
        self._ratio: float = ratio
        self._recipe: str = recipe
        self._selling_type: SellingType = convert_str_to_selling_type(sellingType)
        self._store_quantity_kg: float = storeQuantityKg
