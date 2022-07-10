from quick_resto_objects.modules.core.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
from quick_resto_objects.modules.warehouse.dish_category import convert_str_to_selling_type, DishCategory, SellingType
from quick_resto_objects.modules.warehouse.dish_sale import DishSale
from quick_resto_objects.quick_resto_object import QuickRestoObject


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
    def title(self) -> str:
        return self._title

    @property
    def recipe(self) -> str:
        return self._recipe

    @property
    def selling_type(self) -> SellingType:
        return self._selling_type

    @property
    def store_quantity_kg(self) -> float:
        return self._store_quantity_kg

    @property
    def parent_id(self) -> int:
        return self._parent_id

    @property
    def parent_item(self) -> DishCategory:
        return self._parent_item

    @property
    def store_item_tag(self) -> StoreItemTag:
        return self._store_item_tag

    def __init__(self, article: str = None, basePriceInList: float = None, dishSales: list = None,
                 displayOnTerminal: bool = None,
                 excludeDiscount: bool = None, excludeMarkup: bool = None, measureUnit: dict = None,
                 minimalPrice: float = None, name: str = None,
                 pack: float = None, ratio: float = None, recipe: str = None, sellingType: str = None,
                 storeQuantityKg: float = None, parentId: int = None,
                 parentItem: dict = None, price: float = 0.0, itemTitle: str = "", storeItemTag=None, **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.warehouse.nomenclature.Dish"

        super().__init__(class_name=class_name, **kwargs)
        if (article != None): self._article: int = int(article)
        self._base_price_in_list: float = basePriceInList

        if dishSales is not None:
            self._dish_sales: list = [DishSale(**dish_sale) for dish_sale in dishSales]
        else:
            self._dish_sales = None

        self._display_on_terminal: bool = displayOnTerminal
        self._exclude_discount: bool = excludeDiscount
        self._exclude_markup: bool = excludeMarkup

        if measureUnit is not None: 
            self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        else:
            self._measure_unit = None

        self._minimal_price: float = minimalPrice
        self._name: str = name
        self._pack: float = pack
        self._price: float = price
        self._ratio: float = ratio
        self._recipe: str = recipe
        self._title: str = itemTitle
        self._selling_type: SellingType = convert_str_to_selling_type(sellingType)
        self._store_quantity_kg: float = storeQuantityKg

        if storeItemTag is not None:
            self._store_item_tag = StoreItemTag(**storeItemTag)
        else:
            self._store_item_tag = None

        self._parent_id = parentId

        if parentItem is not None: 
            self._parent_item = DishCategory(**parentItem)
        else:
            self._parent_item = None
