from quick_resto_objects.modules.alcohol.alcohol_dictionary import AlcoholDictionary
from quick_resto_objects.quick_resto_object import QuickRestoObject


class AlcoholReport(QuickRestoObject):
    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def tap_time(self) -> int:
        return self._tap_time

    @property
    def count(self) -> int:
        return self._count

    @property
    def alcohol_dictionary(self) -> AlcoholDictionary:
        return self._alcohol_dictionary

    def __init__(self, deleted: bool = None, tapTime: int = None, count: int = None, alcoholDictionary: dict = None,
                 **kwargs):
        class_name = "ru.edgex.quickresto.modules.alcohol.report.AlcoholReport"

        super().__init__(class_name=class_name, **kwargs)

        self._deleted: bool = deleted
        self._tap_time: int = tapTime
        self._count: int = count
        
        if alcoholDictionary is not None: 
            self._alcohol_dictionary = AlcoholDictionary(**alcoholDictionary)
        else:
            self._alcohol_dictionary = None
