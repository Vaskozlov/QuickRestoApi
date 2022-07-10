from quick_resto_objects.modules.front.table_scheme import TableScheme
from quick_resto_objects.modules.front.device_command import DeviceCommand
from quick_resto_objects.quick_resto_object import QuickRestoObject


class PosTerminal(QuickRestoObject):
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
    def table_scheme(self) -> TableScheme:
        return self._table_scheme

    @property
    def command(self) -> DeviceCommand:
        return self._command

    @property
    def business(self) -> dict:
        return self._business

    @property
    def connection_kind(self) -> str:
        return self._connection_kind

    @property
    def pos_additional_info(self) -> str:
        return self._pos_additional_info

    @property
    def arcus2_protocol(self) -> str:
        return self._arcus2_protocol

    @property
    def pos_printing_type(self) -> str:
        return self._pos_printing_type

    def __init__(self, deviceId: str = None, manufacturer: str = None, model: str = None, connected: bool = None,
                 name: str = None,
                 deleted: bool = None, activateOnCurrentTerminal: bool = None, state: str = None,
                 tableScheme: dict = None, command: dict = None,
                 business: dict = None, connectionKind: str = None, posAdditionalInfo: str = None,
                 arcus2Protocol: str = None,
                 posPrintingType: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.terminals.pos.PosTerminal"

        super().__init__(class_name=class_name, **kwargs)

        self._device_id: str = deviceId
        self._manufacturer: str = manufacturer
        self._model: str = model
        self._connected: bool = connected
        self._name: str = name
        self._deleted: bool = deleted
        self._activate_on_current_terminal: bool = activateOnCurrentTerminal
        self._state: str = state

        if tableScheme is not None: 
            self._table_scheme = TableScheme(**tableScheme)
        else:
            self._table_scheme = None

        if command is not None: 
            self._command = DeviceCommand(**command)
        else:
            self._command = None

        self._business: dict = business
        self._connection_kind: str = connectionKind
        self._pos_additional_info: str = posAdditionalInfo
        self._arcus2_protocol: str = arcus2Protocol
        self._pos_printing_type: str = posPrintingType
