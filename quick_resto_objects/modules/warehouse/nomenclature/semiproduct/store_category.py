from quick_resto_objects.modules.core.dictionaries.measureunits.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.dictionaries.storeitemtag.store_item_tag import StoreItemTag
from quick_resto_objects.quick_resto_object import QuickRestoObject

class StoreCategory(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def measure_unit(self) -> MeasureUnit:
        return self._measure_unit

    @property
    def store_item_tag(self) -> StoreItemTag:
        return self._store_item_tag

    @property
    def color(self) -> str:
        return self._color

    @property
    def display_on_terminal(self) -> bool:
        return self._display_on_terminal

    @property
    def item_title(self) -> str:
        return self._item_title

    def __init__(self, version: int, serverRegisterTime: str, name: str, measureUnit: dict, storeItemTag: dict, color: str, displayOnTerminal: bool, itemTitle: str, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.StoreCategory"
        super().__init__(class_name=class_name, **kwargs)

        self._version: int = version
        self._server_register_time: str = serverRegisterTime
        self._name: str = name
        self._measure_unit: dict = MeasureUnit(**measureUnit)
        self._store_item_tag: dict = StoreItemTag(**storeItemTag)
        self._color: str = color
        self._display_on_terminal: bool = displayOnTerminal
        self._item_title: str = itemTitle