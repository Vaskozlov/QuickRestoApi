from quick_resto_objects.modules.core.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
from quick_resto_objects.modules.warehouse.dish_sale import DishSale
from quick_resto_objects.quick_resto_object import QuickRestoObject


class ModifierGroup(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def measure_unit(self) -> MeasureUnit:
        return self._measure_unit

    @property
    def color(self) -> str:
        return self._color

    @property
    def display_on_terminal(self) -> bool:
        return self._display_on_terminal

    @property
    def min_value(self) -> int:
        return self._min_value

    @property
    def max_value(self) -> int:
        return self._max_value

    @property
    def with_dish(self) -> bool:
        return self._with_dish

    @property
    def modifier_sales(self) -> list:
        return self._modifier_sales

    @property
    def item_title(self) -> str:
        return self._item_title

    @property
    def store_item_tag(self) -> StoreItemTag:
        return self._store_item_tag

    def __init__(self, name: str = None, measureUnit: dict = None, color: str = None, displayOnTerminal: bool = None,
                 minValue: int = None, maxValue: int = None, withDish: bool = None,
                 modifierSales: list = None, itemTitle: str = None, deleted: bool = None, storeItemTag=None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.mods.ModifierGroup"

        super().__init__(class_name=class_name, **kwargs)

        self._name = name
        self._deleted = deleted

        if measureUnit is not None: 
            self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        else:
            self._measure_unit = None

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

        if storeItemTag is not None:
            self._store_item_tag = StoreItemTag(**storeItemTag)
        else:
            self._store_item_tag = None
