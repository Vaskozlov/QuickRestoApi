from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.store.employee import Employee


class Store(QuickRestoObject):
    def __init__(self, liteBusiness: dict, storeCode: str, title: str, **kwargs):
        super().__init__(**kwargs)
        self._store_code: int = int(storeCode)
        self._title: str = title
        self._employee = Employee(**liteBusiness) # TODO: liteBusiness can be list?



