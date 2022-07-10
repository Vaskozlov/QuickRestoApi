from quick_resto_objects.quick_resto_object import QuickRestoObject


class RaspberryTerminal(QuickRestoObject):
    @property
    def code1_c(self) -> str:
        return self._code1_c

    @property
    def device_id(self) -> str:
        return self._device_id

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
    def deleted(self) -> bool:
        return self._deleted

    @property
    def name(self) -> str:
        return self._name

    @property
    def serial_number(self) -> str:
        return self._serial_number

    @property
    def hardware_version(self) -> str:
        return self._hardware_version

    @property
    def last_sync_time(self) -> str:
        return self._last_sync_time

    @property
    def software_version(self) -> str:
        return self._software_version

    @property
    def product(self) -> str:
        return self._product

    @property
    def online(self) -> bool:
        return self._online

    def __init__(self, code1C: str, deviceId: str, macAddress: str, manufacturer: str, model: str, connected: bool,
                 deleted: bool, name: str, serialNumber: str, hardwareVersion: str, lastSyncTime: str,
                 softwareVersion: str, product: str, online: bool, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.terminals.raspberry.RaspberryTerminal"

        super().__init__(class_name=class_name, **kwargs)

        self._code1_c: str = code1C
        self._device_id: str = deviceId
        self._mac_address: str = macAddress
        self._manufacturer: str = manufacturer
        self._model: str = model
        self._connected: bool = connected
        self._deleted: bool = deleted
        self._name: str = name
        self._serial_number: str = serialNumber
        self._hardware_version: str = hardwareVersion
        self._last_sync_time: str = lastSyncTime
        self._software_version: str = softwareVersion
        self._product: str = product
        self._online: bool = online
