from enum import Enum
from quick_resto_objects.modules.front.kkm_terminal import KkmTerminal

from quick_resto_objects.quick_resto_object import QuickRestoObject


class ShiftStatus(Enum):
    OPENED = "OPENED"
    CLOSE = "CLOSE"
    NONE = "NONE"


StrToShiftStatus = {
    ShiftStatus.OPENED.value: ShiftStatus.OPENED,
    ShiftStatus.CLOSE.value: ShiftStatus.CLOSE,
}


def convert_str_to_system_Unit(value: str) -> ShiftStatus:
    if value in StrToShiftStatus.keys():
        return StrToShiftStatus[value]

    return ShiftStatus.NONE


class Shift(QuickRestoObject):
    @property
    def cash_out_cheks_count(self) -> int:
        return self._cash_out_cheks_count

    @property
    def cash_in_cheks_count(self) -> int:
        return self._cash_in_cheks_count

    @property
    def close_cash_in_register(self) -> int:
        return self._close_cash_in_register

    @property
    def closer_id(self) -> int:
        return self._closer_id

    @property
    def closed(self) -> int:
        return self._closed

    @property
    def code1_c(self) -> str:
        return self._code1_c

    @property
    def incomplete(self) -> bool:
        return self._incomplete

    @property
    def kkm_terminal(self) -> KkmTerminal:
        return self._kkm_terminal

    @property
    def non_fiscal_total_bonuses(self) -> int:
        return self._non_fiscal_total_bonuses

    @property
    def non_fiscal_total_card(self) -> int:
        return self._non_fiscal_total_card

    @property
    def non_fiscal_total_cash(self) -> int:
        return self._non_fiscal_total_cash

    @property
    def non_fiscal_total_return_bonuses(self) -> int:
        return self._non_fiscal_total_return_bonuses

    @property
    def non_fiscal_total_return_card(self) -> int:
        return self._non_fiscal_total_return_card

    @property
    def non_fiscal_total_return_cash(self) -> int:
        return self._non_fiscal_total_return_cash

    @property
    def open_cash_in_register(self) -> int:
        return self._open_cash_in_register

    @property
    def opened(self) -> int:
        return self._opened

    @property
    def opener_id(self) -> str:
        return self._opener_id

    @property
    def orders_count(self) -> int:
        return self._orders_count

    @property
    def return_orders_count(self) -> int:
        return self._return_orders_count

    @property
    def shift_number(self) -> int:
        return self._shift_number

    @property
    def status(self) -> ShiftStatus:
        return self._status

    @property
    def total_card(self) -> int:
        return self._total_card

    @property
    def total_cash(self) -> int:
        return self._total_cash

    @property
    def total_cash_in(self) -> int:
        return self._total_cash_in

    @property
    def total_cash_in_register(self) -> int:
        return self._total_cash_in_register

    @property
    def total_cash_out(self) -> int:
        return self._total_cash_out

    @property
    def total_return_bonuses(self) -> int:
        return self._total_return_bonuses

    @property
    def total_return_card(self) -> int:
        return self._total_return_card

    @property
    def total_return_cash(self) -> int:
        return self._total_return_cash

    @property
    def write_off_total_bonuses(self) -> int:
        return self._write_off_total_bonuses

    @property
    def write_off_total_card(self) -> int:
        return self._write_off_total_card

    @property
    def write_off_total_cash(self) -> int:
        return self._write_off_total_cash

    @property
    def write_off_total_return_bonuses(self) -> int:
        return self._write_off_total_return_bonuses

    @property
    def write_off_total_return_card(self) -> int:
        return self._write_off_total_return_card

    @property
    def write_off_total_return_cash(self) -> int:
        return self._write_off_total_return_cash

    @property
    def z_report_document_number(self) -> int:
        return self._z_report_document_number

    def __init__(self, cashOutCheksCount: int = None, cashInCheksCount: int = None, closeCashInRegister: int = None,
                 closerId: int = None, closed: int = None,
                 code1C: str = None, incomplete: bool = None, kkmTerminal: dict = None,
                 nonFiscalTotalBonuses: int = None, nonFiscalTotalCard: int = None,
                 nonFiscalTotalCash: int = None, nonFiscalTotalReturnBonuses: int = None,
                 nonFiscalTotalReturnCard: int = None,
                 nonFiscalTotalReturnCash: int = None, openCashInRegister: int = None, opened: int = None,
                 openerId: str = None, ordersCount: int = None,
                 returnOrdersCount: int = None, shiftNumber: int = None, status: str = None, totalCard: int = None,
                 totalCash: int = None, totalCashIn: int = None,
                 totalCashInRegister: int = None, totalCashOut: int = None, totalReturnBonuses: int = None,
                 totalReturnCard: int = None, totalReturnCash: int = None,
                 writeOffTotalBonuses: int = None, writeOffTotalCard: int = None, writeOffTotalCash: int = None,
                 writeOffTotalReturnBonuses: int = None,
                 writeOffTotalReturnCard: int = None, writeOffTotalReturnCash: int = None,
                 zReportDocumentNumber: int = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.zreport.Shift"

        super().__init__(class_name=class_name, **kwargs)

        self._cash_out_cheks_count: int = cashOutCheksCount
        self._cash_in_cheks_count: int = cashInCheksCount
        self._close_cash_in_register: int = closeCashInRegister
        self._closer_id: int = closerId
        self._closed: int = closed
        self._code1_c: str = code1C
        self._incomplete: bool = incomplete

        if kkmTerminal is not None:
            self._kkm_terminal = KkmTerminal(**kkmTerminal)
        else:
            self._kkm_terminal = None

        self._non_fiscal_total_bonuses: int = nonFiscalTotalBonuses
        self._non_fiscal_total_card: int = nonFiscalTotalCard
        self._non_fiscal_total_cash: int = nonFiscalTotalCash
        self._non_fiscal_total_return_bonuses: int = nonFiscalTotalReturnBonuses
        self._non_fiscal_total_return_card: int = nonFiscalTotalReturnCard
        self._non_fiscal_total_return_cash: int = nonFiscalTotalReturnCash
        self._open_cash_in_register: int = openCashInRegister
        self._opened: int = opened
        self._opener_id: str = openerId
        self._orders_count: int = ordersCount
        self._return_orders_count: int = returnOrdersCount
        self._shift_number: int = shiftNumber
        self._status: dict = convert_str_to_system_Unit(status)
        self._total_card: int = totalCard
        self._total_cash: int = totalCash
        self._total_cash_in: int = totalCashIn
        self._total_cash_in_register: int = totalCashInRegister
        self._total_cash_out: int = totalCashOut
        self._total_return_bonuses: int = totalReturnBonuses
        self._total_return_card: int = totalReturnCard
        self._total_return_cash: int = totalReturnCash
        self._write_off_total_bonuses: int = writeOffTotalBonuses
        self._write_off_total_card: int = writeOffTotalCard
        self._write_off_total_cash: int = writeOffTotalCash
        self._write_off_total_return_bonuses: int = writeOffTotalReturnBonuses
        self._write_off_total_return_card: int = writeOffTotalReturnCard
        self._write_off_total_return_cash: int = writeOffTotalReturnCash
        self._z_report_document_number: int = zReportDocumentNumber
