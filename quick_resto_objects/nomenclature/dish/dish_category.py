from enum import Enum
from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.nomenclature.dish.dish_sales import DishSale
from quick_resto_objects.measureunits.measure_unit import MeasureType, MeasureUnit


class SellingType(Enum):
    WHOLE = "WHOLE"
    NONE = "NONE"


StrToSellingType = {
    SellingType.WHOLE.value: SellingType.WHOLE
}


def convert_str_to_selling_type(selling_type: str) -> SellingType:
    if selling_type in StrToSellingType.keys():
        return StrToSellingType[selling_type]

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
    def measure_type(self) -> MeasureType:
        return self.measure_unit.measure_type

    @property
    def selling_type(self) -> SellingType:
        return self._selling_type

    def __init__(self, itemTitle: str, name: str, displayOnTerminal: bool, color: str, sellingType: str,
                 measureUnit: dict, dishSales=None, **kwargs):
        class_name: str = "modules.core.dictionaries.measureunits.MeasureUnit"

        super().__init__(class_name=class_name, **kwargs)
        self._title: str = itemTitle
        self._name: str = name
        self._color: str = color
        self._display_on_terminal: bool = displayOnTerminal
        self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        self._selling_type: SellingType = convert_str_to_selling_type(sellingType)

        if dishSales is None:
            self._dish_sales = None
        else:
            self._dish_sales: list = [DishSale(**dish_sale) for dish_sale in dishSales]
