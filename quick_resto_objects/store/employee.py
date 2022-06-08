from quick_resto_objects.quick_resto_object import QuickRestoObject


class Employee(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def nds(self) -> bool:
        return self._nds

    @property
    def short_name(self) -> str:
        return self._short_name

    def __init__(self, name: str, nds: bool, shortName: str, **kwargs):
        super().__init__(className="modules.warehouse.store.employee.Employee", **kwargs)
        self._name: str = name
        self._nds: bool = nds
        self._short_name: str = shortName
