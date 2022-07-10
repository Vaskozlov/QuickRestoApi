from quick_resto_objects.modules.core.measure_unit import MeasureUnit
from quick_resto_objects.quick_resto_object import QuickRestoObject

class PackingUnit(QuickRestoObject):
    @property
    def version(self) -> int:
        return self._version

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent_ratio(self) -> float:
        return self._parent_ratio

    @property
    def parent_unit(self) -> MeasureUnit:
        return self._parent_unit

    def __init__(self, version: int = None, name: str = None, parentRatio: float = None, parentUnit: dict = None,
                 **kwargs):
        class_name = "ru.edgex.quickresto.modules.core.dictionaries.packingunits.PackingUnit"

        super().__init__(class_name=class_name, **kwargs)

        self._version: int = version
        self._name: str = name
        self._parent_ratio: float = parentRatio

        if parentUnit is not None: 
            self._parent_unit = MeasureUnit(**parentUnit)
        else:
            self._parent_unit = None
