from quick_resto_objects.modules.front.terminal import Terminal
from quick_resto_objects.modules.warehouse.store import Store
from quick_resto_objects.quick_resto_object import QuickRestoObject


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

    @property
    def backup_target_device(self) -> Terminal:
        return self._backup_target_device

    @property
    def doublicating_target_Device(self) -> Terminal:
        return self._doublicating_target_Device

    @property
    def target_Device(self) -> Terminal:
        return self._target_Device

    def __init__(self, sendSignal: bool = None, title: str = None, store: dict = None, backupTargetDevice: dict = None,
                 doublicatingTargetDevice: dict = None, targetDevice: dict = None, **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.warehouse.nomenclature.cooking_place.CookingPlace"

        super().__init__(class_name=class_name, **kwargs)
        self._send_signal = sendSignal
        self._title = title

        if backupTargetDevice is not None: 
            self._backup_target_device = Terminal(**backupTargetDevice)
        else:
            self._backup_target_device = None

        if targetDevice is not None: 
            self._target_Device = Terminal(**targetDevice)
        else:
            self._target_Device = None

        if store is not None:
            self._store = Store(**store)
        else:
            self._store = None

        if doublicatingTargetDevice is not None:
            self._doublicating_target_Device = Terminal(**doublicatingTargetDevice)
        else:
            self._doublicating_target_Device = None
