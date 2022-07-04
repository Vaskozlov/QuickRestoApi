from quick_resto_objects.modules.core.dictionaries.measureunits.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.dictionaries.storeitemtag.store_item_tag import StoreItemTag
from quick_resto_objects.quick_resto_object import QuickRestoObject

class SemiProduct(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def article(self) -> str:
        return self._article

    @property
    def measure_unit(self) -> MeasureUnit:
        return self._measure_unit

    @property
    def store_item_tag(self) -> StoreItemTag:
        return self._store_item_tag

    @property
    def ratio(self) -> float:
        return self._ratio

    @property
    def minimal_price(self) -> float:
        return self._minimal_price

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
    def limit(self) -> float:
        return self._limit

    @property
    def item_title(self) -> str:
        return self._item_title

    @property
    def base_price_in_list(self) -> float:
        return self._base_price_in_list

    @property
    def pack(self) -> float:
        return self._pack

    @property
    def recipe(self) -> str:
        return self._recipe

    def __init__(self, version: int, serverRegisterTime: str, name: str, article: str, measureUnit: dict, storeItemTag: dict, 
                ratio: float, minimalPrice: float, excludeDiscount: bool, excludeMarkup: bool, storeQuantityKg: float, 
                limit: float, itemTitle: str, basePriceInList: float, pack: float, recipe: str, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.semiproduct.SemiProduct"
        super().__init__(class_name=class_name, **kwargs)

        self._version: int = version
        self._server_register_time: str = serverRegisterTime
        self._name: str = name
        self._article: str = article
        self._measure_unit: dict = MeasureUnit(**measureUnit)
        self._store_item_tag: dict = StoreItemTag(**storeItemTag)
        self._ratio: float = ratio
        self._minimal_price: float = minimalPrice
        self._exclude_discount: bool = excludeDiscount
        self._exclude_markup: bool = excludeMarkup
        self._store_quantity_kg: float = storeQuantityKg
        self._limit: float = limit
        self._item_title: str = itemTitle
        self._base_price_in_list: float = basePriceInList
        self._pack: float = pack
        self._recipe: str = recipe