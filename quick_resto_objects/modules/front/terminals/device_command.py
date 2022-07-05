from enum import Enum

from quick_resto_objects.quick_resto_object import QuickRestoObject


class DeviceState(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    NONE = "NONE"


StrToDeviceState = {
    DeviceState.ACTIVE.value: DeviceState.ACTIVE,
    DeviceState.INACTIVE.value: DeviceState.INACTIVE,
}


def convert_str_to_device_state(value: str) -> DeviceState:
    if value in StrToDeviceState.keys():
        return StrToDeviceState[value]

    return DeviceState.NONE


class DeviceCommand(QuickRestoObject):
    @property
    def version(self) -> int:
        return self._version

    @property
    def state(self) -> DeviceState:
        return self._state

    def __init__(self, version: int = None, state: str = None, **kwargs):
        class_name = ""
        super().__init__(class_name=class_name, **kwargs)

        self._version: int = version
        self._state = convert_str_to_device_state(state)
