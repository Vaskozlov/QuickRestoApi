from quick_resto_objects.modules.core.measure_unit import MeasureUnit
from quick_resto_objects.modules.core.store_item_tag import StoreItemTag
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

    def __init__(self, version: int = None, serverRegisterTime: str = None, name: str = None, measureUnit: dict = None,
                 storeItemTag: dict = None,
                 color: str = None, displayOnTerminal: bool = None, itemTitle: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.StoreCategory"
        super().__init__(class_name=class_name, **kwargs)

        self._version: int = version
        self._server_register_time: str = serverRegisterTime
        self._name: str = name

        if measureUnit is not None: 
            self._measure_unit: MeasureUnit = MeasureUnit(**measureUnit)
        else:
            self._measure_unit = None

        if storeItemTag is not None:
            self._store_item_tag = StoreItemTag(**storeItemTag)
        else:
            self._store_item_tag = None
            
        self._color: str = color
        self._display_on_terminal: bool = displayOnTerminal
        self._item_title: str = itemTitle
