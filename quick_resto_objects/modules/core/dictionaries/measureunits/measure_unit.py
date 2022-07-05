from enum import Enum

from quick_resto_objects.quick_resto_object import QuickRestoObject


class SystemUnit(Enum):
    ITEM = "ITEM",
    KG = "KG",
    L = "L",
    RATION = "RATION",
    Custom = "Custom"


StrToSystemUnit = {
    SystemUnit.ITEM.value: SystemUnit.ITEM,
    SystemUnit.KG.value: SystemUnit.KG,
    SystemUnit.L.value: SystemUnit.L,
    SystemUnit.RATION.value: SystemUnit.RATION,
    SystemUnit.Custom.value: SystemUnit.Custom
}


def convert_str_to_system_unit(value: str) -> SystemUnit:
    if value in StrToSystemUnit.keys():
        return StrToSystemUnit[value]

    return SystemUnit.Custom


class MeasureUnit(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def parent_ratio(self) -> float:
        return self._parent_ratio

    @property
    def system_unit(self) -> SystemUnit:
        return self._system_unit

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def is_main_unit(self) -> bool:
        return self._is_main_unit

    @property
    def code(self) -> str:
        return self._code

    def __init__(self, name: str = None, fullName: str = None, isMainUnit: bool = None, parentRatio: float = None,
                 code: str = None,
                 systemUnit: str = "ITEM", **kwargs):
        class_name = "ru.edgex.quickresto.modules.core.dictionaries.measureunits.MeasureUnit"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._parent_ratio: float = parentRatio
        self._system_unit = convert_str_to_system_unit(systemUnit)
        self._full_name: str = fullName
        self._is_main_unit: bool = isMainUnit
        self._code: str = code
