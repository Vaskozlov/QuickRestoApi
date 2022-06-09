from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.store.store import Store


class CookingPlace(QuickRestoObject):
    @property
    def send_signal(self) -> bool:
        return self._send_signal

    @property
    def store(self) -> Store:
        return self._store

    @property
    def title(self) -> str:
        return self._title

    def __init__(self, sendSignal: bool, store: dict, title: str, **kwargs):
        class_name: str = "modules.warehouse.nomenclature.cookingPlace"

        super().__init__(class_name=class_name, **kwargs)
        self._send_signal: bool = sendSignal
        self._store: Store = Store(**store)
        self._title: str = title
