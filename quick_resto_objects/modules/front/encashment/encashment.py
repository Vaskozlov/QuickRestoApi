from enum import Enum

from quick_resto_objects.modules.front.zreport.shift import Shift
from quick_resto_objects.modules.personnel.employee.employee import Employee
from quick_resto_objects.modules.warehouse.nomenclature.sale_place.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class EncashmentType(Enum):
    CASHIN = "CASHIN"
    CASHOUT = "CASHOUT"
    NONE = "NONE"


StrToEncashmentType = {
    EncashmentType.CASHIN.value: EncashmentType.CASHIN,
    EncashmentType.CASHOUT.value: EncashmentType.CASHOUT,
}


def convert_str_to__encashment_Type(value: str) -> EncashmentType:
    if value in StrToEncashmentType.keys():
        return StrToEncashmentType[value]

    return EncashmentType.NONE


class Encashment(QuickRestoObject):
    @property
    def time_encashment(self) -> str:
        return self._time_encashment

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def number(self) -> int:
        return self._number

    @property
    def boolean(self) -> bool:
        return self._boolean

    @property
    def employee(self) -> Employee:
        return self._employee

    @property
    def kkm(self) -> dict:
        return self._kkm

    @property
    def _sale_place(self) -> SalePlace:
        return self.__sale_place

    @property
    def shift(self) -> Shift:
        return self._shift

    @property
    def type_transaction(self) -> EncashmentType:
        return self._type_transaction

    def __init__(self, timeEncashment: str = None, amount: int = None, number: int = None, boolean: bool = None,
                 employee: dict = None, kkm: dict = None, salePlace: dict = None,
                 shift: dict = None, typeTransaction: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.encashment.Encashment"

        super().__init__(class_name=class_name, **kwargs)

        self._time_encashment: str = timeEncashment
        self._amount: int = amount
        self._number: int = number
        self._boolean: bool = boolean
        if (employee != None): self._employee = Employee(**employee)
        if (kkm != None): self._kkm: dict = kkm
        if (salePlace != None): self.__sale_place = SalePlace(**salePlace)
        if (shift != None): self._shift = Shift(**shift)
        self._type_transaction = convert_str_to__encashment_Type(typeTransaction)
