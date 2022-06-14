from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.store.employee import Employee


class Store(QuickRestoObject):
    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    @property
    def store_code(self) -> int:
        return self._store_code

    @property
    def employee(self) -> Employee:
        return self._employee

    def __init__(self, liteBusiness: dict, storeCode: str, title: str, description: str = "", **kwargs):
        class_name: str = "modules.warehouse.store"

        super().__init__(class_name=class_name, **kwargs)
        self._title: str = title
        self._description: str = description
        self._store_code: int = int(storeCode)
        self._employee = Employee(**liteBusiness)  # TODO: liteBusiness can be list?
