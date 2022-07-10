from enum import Enum

from quick_resto_objects.modules.core.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
from quick_resto_objects.modules.warehouse.dish_sale import DishSale
from quick_resto_objects.quick_resto_object import QuickRestoObject


class SellingType(Enum):
    WHOLE = "WHOLE"
    PART = "PART"
    WEIGHT = "WEIGHT"
    NONE = "NONE"


StrToSellingType = {
    SellingType.WHOLE.value: SellingType.WHOLE,
    SellingType.PART.value: SellingType.PART,
    SellingType.WEIGHT.value: SellingType.WEIGHT
}


def convert_str_to_selling_type(value: str) -> SellingType:
    if value in StrToSellingType.keys():
        return StrToSellingType[value]

    return SellingType.NONE


class DishCategory(QuickRestoObject):
    @property
    def title(self) -> str:
        return self._title

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> str:
        return self._color

    @property
    def display_on_terminal(self) -> bool:
        return self._display_on_terminal

    @property
    def measure_unit(self) -> MeasureUnit:
        return self._measure_unit

    @property
    def selling_type(self) -> SellingType:
        return self._selling_type

    @property
    def dish_sales(self) -> list:
        return self._dish_sales

    @property
    def store_item_tag(self) -> StoreItemTag:
        return self._store_item_tag

    def __init__(self, itemTitle: str = None, name: str = None, displayOnTerminal: bool = None, color: str = None,
                 sellingType: str = None,
                 measureUnit: dict = None, dishSales=None, storeItemTag=None, **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.warehouse.nomenclature.dish.DishCategory"

        super().__init__(class_name=class_name, **kwargs)
        self._title: str = itemTitle
        self._name: str = name
        self._color: str = color
        self._display_on_terminal: bool = displayOnTerminal

        if measureUnit is not None: 
            self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        else:
            self._measure_unit = None

        self._selling_type: SellingType = convert_str_to_selling_type(sellingType)

        if storeItemTag is not None:
            self._store_item_tag = StoreItemTag(**storeItemTag)
        else:
            self._store_item_tag = None

        if dishSales is not None:
            self._dish_sales: list = [DishSale(**dish_sale) for dish_sale in dishSales]
        else:
            self._dish_sales = None
