from enum import Enum

from quick_resto_objects.modules.front.table_scheme import TableScheme
from quick_resto_objects.modules.front.device_command import DeviceCommand
from quick_resto_objects.modules.warehouse.organization import Organization
from quick_resto_objects.quick_resto_object import QuickRestoObject


class HardwareState(Enum):
    NEW = "NEW"
    INACTIVE = "INACTIVE"
    ACTIVATING = "ACTIVATING"
    ACTIVE = "ACTIVE"
    DEACTIVATIN = "DEACTIVATING"
    DELETED = "DELETED"
    NONE = "NONE"


StrToHardwareState = {
    HardwareState.NEW.value: HardwareState.NEW,
    HardwareState.INACTIVE.value: HardwareState.INACTIVE,
    HardwareState.ACTIVATING.value: HardwareState.ACTIVATING,
    HardwareState.ACTIVE.value: HardwareState.ACTIVE,
    HardwareState.DEACTIVATIN.value: HardwareState.DEACTIVATIN,
    HardwareState.DELETED.value: HardwareState.DELETED,
}


def convert_str_to_hardware_state(value: str) -> HardwareState:
    if value in StrToHardwareState.keys():
        return StrToHardwareState[value]

    return HardwareState.NONE


class TicketDevice(QuickRestoObject):
    @property
    def code1_c(self) -> str:
        return self._code1_c

    @property
    def mac_address(self) -> str:
        return self._mac_address

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
    def device_id(self) -> str:
        return self._device_id

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def name(self) -> str:
        return self._name

    @property
    def serial_number(self) -> str:
        return self._serial_number

    @property
    def command(self) -> DeviceCommand:
        return self._command

    @property
    def table_scheme(self) -> TableScheme:
        return self._table_scheme

    @property
    def business(self) -> dict:
        return self._business

    @property
    def state(self) -> HardwareState:
        return self._state

    @property
    def kkm_mode(self) -> bool:
        return self._kkm_mode

    @property
    def symbols_per_line(self) -> int:
        return self._symbols_per_line

    @property
    def organization(self) -> Organization:
        return self._organization

    def __init__(self, code1C: str = None, macAddress: str = None, manufacturer: str = None, model: str = None,
                 connected: bool = None,
                 deviceId: str = None, deleted: bool = None, name: str = None, serialNumber: str = None,
                 command: dict = None, tableScheme: dict = None,
                 business: dict = None, state: str = None, kkmMode: bool = None, symbolsPerLine: int = None,
                 organization: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.terminals.ticketdevices.TicketDevice"

        super().__init__(class_name=class_name, **kwargs)

        self._code1_c: str = code1C
        self._mac_address: str = macAddress
        self._manufacturer: str = manufacturer
        self._model: str = model
        self._connected: bool = connected
        self._device_id: str = deviceId
        self._deleted: bool = deleted
        self._name: str = name
        self._serial_number: str = serialNumber

        if tableScheme is not None: 
            self._table_scheme = TableScheme(**tableScheme)
        else:
            self._table_scheme = None

        if tableScheme is not None: 
            self._table_scheme = TableScheme(**tableScheme)
        else:
            self._table_scheme = None

        self._business: dict = business
        self._state = convert_str_to_hardware_state(state)
        self._kkm_mode: bool = kkmMode
        self._symbols_per_line: int = symbolsPerLine

        if organization is not None: 
            self._organization = Organization(**organization)
        else:
            self._organization = None
