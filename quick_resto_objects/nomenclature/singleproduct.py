from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.measureunits.measure_unit import MeasureUnit


class SingleProduct(QuickRestoObject):
    @property
    def article(self) -> int:
        return self._article

    @property
    def base_price_in_list(self) -> float:
        return self._base_price_in_list

    @property
    def exclude_discount(self) -> bool:
        return self._exclude_discount

    @property
    def exclude_markup(self) -> bool:
        return self._exclude_markup

    @property
    def item_title(self) -> str:
        return self._item_title

    @property
    def limit(self) -> float:
        return self._limit

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
    def ratio(self) -> float:
        return self._ratio

    @property
    def recipe(self) -> str:
        return self._recipe

    @property
    def store_quantity_kg(self) -> float:
        return self._store_quantity_kg

    def __init__(self, article: str, basePriceInList: float, excludeDiscount: bool, excludeMarkup: bool, itemTitle: str,
                 limit: float, measureUnit: dict, minimalPrice: float, name: str, pack: float, recipe: str,
                 storeQuantityKg: float, ratio: float, **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.nomenclature.singleproduct"

        super().__init__(class_name=class_name, **kwargs)
        self._article: int = int(article)
        self._base_price_in_list: float = basePriceInList
        self._exclude_discount: bool = excludeDiscount
        self._exclude_markup: bool = excludeMarkup
        self._item_title: str = itemTitle
        self._limit: float = limit
        self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        self._minimal_price: float = minimalPrice
        self._name: str = name
        self._pack: float = pack
        self._ratio: float = ratio
        self._recipe: str = recipe
        self._store_quantity_kg: float = storeQuantityKg
