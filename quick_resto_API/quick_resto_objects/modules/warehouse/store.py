from quick_resto_objects.modules.warehouse.employee import Employee
from quick_resto_objects.quick_resto_object import QuickRestoObject


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
    def lite_business(self) -> Employee:
        return self._lite_business

    def __init__(self, storeCode: str = None, title: str = None, liteBusiness: dict = None, description: str = "",
                 **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.warehouse.store.Store"

        super().__init__(class_name=class_name, **kwargs)
        self._title: str = title
        self._description: str = description
        self._store_code: int = int(storeCode)
        
        if liteBusiness is not None:
            self._lite_business: Employee = Employee(**liteBusiness)
        else:
            self._lite_business = None
