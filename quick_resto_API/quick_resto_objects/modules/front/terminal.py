from enum import Enum

from quick_resto_objects.modules.front.table_scheme import TableScheme
from quick_resto_objects.modules.warehouse.cooking_place import CookingPlace
from quick_resto_objects.modules.warehouse.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class TerminalSubtype(Enum):
    REGISTER = "REGISTER"
    WAITER = "WAITER"
    NONE = "NONE"


class TerminalType(Enum):
    QUICK_POS = "QUICK_POS"
    QUICK_RESTO = "QUICK_RESTO"
    KITCHEN = "KITCHEN"
    NONE = "NONE"


StrToTerminalSubtype = {
    TerminalSubtype.REGISTER.value: TerminalSubtype.REGISTER,
    TerminalSubtype.WAITER.value: TerminalSubtype.WAITER,
}

StrToTerminalType = {
    TerminalType.QUICK_POS.value: TerminalType.QUICK_POS,
    TerminalType.QUICK_RESTO.value: TerminalType.QUICK_RESTO,
    TerminalType.KITCHEN.value: TerminalType.KITCHEN,
}


def convert_str_to_terminal_subtype(value: str) -> TerminalSubtype:
    if value in StrToTerminalSubtype.keys():
        return StrToTerminalSubtype[value]

    return TerminalSubtype.NONE


def convert_str_to_terminal_type(value: str) -> TerminalType:
    if value in StrToTerminalType.keys():
        return StrToTerminalType[value]

    return TerminalType.NONE


class Terminal(QuickRestoObject):
    @property
    def cooking_place(self) -> CookingPlace:
        return self._cooking_place

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def device_manufacturer(self) -> str:
        return self._device_manufacturer

    @property
    def device_model(self) -> str:
        return self._device_model

    @property
    def last_sync(self) -> str:
        return self._last_sync

    @property
    def name(self) -> str:
        return self._name

    @property
    def online(self) -> bool:
        return self._online

    @property
    def registration_date(self) -> str:
        return self._registration_date

    @property
    def sale_place(self) -> SalePlace:
        return self._sale_place

    @property
    def short_name(self) -> str:
        return self._short_name

    @property
    def table_scheme(self) -> dict:
        return self._table_scheme

    @property
    def terminal_subtype(self) -> TerminalSubtype:
        return self._terminal_subtype

    @property
    def terminal_type(self) -> TerminalType:
        return self._terminal_type

    def __init__(self, cookingPlace: dict = None, deleted: bool = None, deviceManufacturer: str = None,
                 deviceModel: str = None,
                 lastSync: str = None, name: str = None, online: bool = None, registrationDate: str = None,
                 salePlace: dict = None,
                 shortName: str = None, tableScheme: dict = None, terminalSubtype: dict = None,
                 terminalType: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.terminals.ipad.Terminal"

        super().__init__(class_name=class_name, **kwargs)

        if cookingPlace is not None: 
            self._cooking_place = CookingPlace(**cookingPlace)
        else:
            self._cooking_place = None

        self._deleted: bool = deleted
        self._device_manufacturer: str = deviceManufacturer
        self._device_model: str = deviceModel
        self._last_sync: str = lastSync
        self._name: str = name
        self._online: bool = online
        self._registration_date: str = registrationDate

        if salePlace is not None: 
            self._sale_place = SalePlace(**salePlace)
        else:
            self._sale_place = None

        self._short_name: str = shortName

        if tableScheme is not None: 
            self._table_scheme = TableScheme(**tableScheme)
        else:
            self._table_scheme = None

        self._terminal_subtype = convert_str_to_terminal_subtype(terminalSubtype)
        self._terminal_type = convert_str_to_terminal_type(terminalType)
