from quick_resto_objects.modules.front.terminals.terminal_device import TerminalDevice
from quick_resto_objects.modules.warehouse.store.store import Store
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
    def backup_target_device(self) -> TerminalDevice:
        return self._backup_target_device

    @property
    def doublicating_target_Device(self) -> TerminalDevice:
        return self._doublicating_target_Device

    @property
    def target_Device(self) -> TerminalDevice:
        return self._target_Device

    def __init__(self, sendSignal: bool, title: str, store: dict, backupTargetDevice:dict = None, 
                    doublicatingTargetDevice:dict = None, targetDevice:dict = None, **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.warehouse.nomenclature.cooking_place.CookingPlace"

        super().__init__(class_name=class_name, **kwargs)
        self._send_signal: bool = sendSignal
        self._store: Store = Store(**store)
        self._title: str = title

        self._backup_target_device = backupTargetDevice
        self._doublicating_target_Device = doublicatingTargetDevice
        self._target_Device = targetDevice
