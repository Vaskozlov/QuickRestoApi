from enum import Enum
from quick_resto_objects.quick_resto_object import *


class MeasureType(Enum):
    NONE = 0
    THING = 1
    KILOGRAM = 2
    LITER = 3
    PORTION = 4


IdToMeasureType = {
    MeasureType.THING.value: MeasureType.THING,
    MeasureType.KILOGRAM.value: MeasureType.KILOGRAM,
    MeasureType.LITER.value: MeasureType.LITER,
    MeasureType.PORTION.value: MeasureType.PORTION
}


def convert_id_to_measure_unit(measure_unit_id: id) -> IdToMeasureType:
    if measure_unit_id in IdToMeasureType.keys():
        return IdToMeasureType[measure_unit_id]

    return MeasureType.NONE


class MeasureUnit(QuickRestoObject):
    @property
    def measure_type(self) -> MeasureType:
        return self._measure_type

    def __init__(self, id: int, className: str):
        super().__init__(id, className)
        self._measure_type: MeasureType = convert_id_to_measure_unit(id)
