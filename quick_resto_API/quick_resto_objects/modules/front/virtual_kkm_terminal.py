from quick_resto_objects.modules.front.device_command import DeviceCommand
from quick_resto_objects.quick_resto_object import QuickRestoObject


class VirtualKkmTerminal(QuickRestoObject):
    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @property
    def model(self) -> str:
        return self._model

    @property
    def connected(self) -> bool:
        return self._connected

    @property
    def name(self) -> str:
        return self._name

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def activate_on_current_terminal(self) -> bool:
        return self._activate_on_current_terminal

    @property
    def state(self) -> str:
        return self._state

    @property
    def command(self) -> DeviceCommand:
        return self._command

    def __init__(self, deviceId: str = None, manufacturer: str = None, model: str = None, connected: bool = None,
                 name: str = None, deleted: bool = None,
                 activateOnCurrentTerminal: bool = None, state: str = None, command: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.terminals.kkm.VirtualKkmTerminal"

        super().__init__(class_name=class_name, **kwargs)

        self._device_id: str = deviceId
        self._manufacturer: str = manufacturer
        self._model: str = model
        self._connected: bool = connected
        self._name: str = name
        self._deleted: bool = deleted
        self._activate_on_current_terminal: bool = activateOnCurrentTerminal
        self._state: str = state

        if command is not None: 
            self._command = DeviceCommand(**command)
        else:
            self._command = None
