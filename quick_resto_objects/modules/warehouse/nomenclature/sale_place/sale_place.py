from quick_resto_objects.modules.front.tablemanagement.table_scheme import TableScheme
from quick_resto_objects.modules.front.terminals.terminal_device import TerminalDevice
from quick_resto_objects.modules.warehouse.nomenclature.cooking_place.cooking_place import CookingPlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class SalePlace(QuickRestoObject):
    @property
    def automatic_encashment(self) -> bool:
        return self._automatic_encashment

    @property
    def can_hold_table_orders(self) -> bool:
        return self._can_hold_table_orders

    @property
    def default_cooking_place(self) -> CookingPlace:
        return self._default_cooking_place

    @property
    def max_table_order_number_enable(self) -> bool:
        return self._max_table_order_number_enable

    @property
    def open_cash_box_on_guest_tickets(self) -> bool:
        return self._open_cash_box_on_guest_tickets

    @property
    def open_cash_box_on_prechecks(self) -> bool:
        return self._open_cash_box_on_prechecks

    @property
    def open_cash_box_on_reports(self) -> bool:
        return self._open_cash_box_on_reports

    @property
    def print_guest_ticket(self) -> bool:
        return self._print_guest_ticket

    @property
    def print_kitchen_ticket(self) -> bool:
        return self._print_kitchen_ticket

    @property
    def services(self) -> list:
        return self._services

    @property
    def title(self) -> str:
        return self._title

    @property
    def table(self) -> TableScheme:
        return self._table

    @property
    def backup_prechecks_target_device(self) -> TerminalDevice:
        return self._backup_prechecks_target_device

    @property
    def kkm_organization1(self) -> TerminalDevice:
        return self._kkm_organization1

    @property
    def kkm_organization2(self) -> TerminalDevice:
        return self._kkm_organization2

    @property
    def prechecks_target_device(self) -> TerminalDevice:
        return self._prechecks_target_device

    @property
    def report_target_device(self) -> TerminalDevice:
        return self._report_target_device

    def __init__(self, automaticEncashment: bool, canHoldTableOrders: bool, defaultCookingPlace: dict,
                 maxTableOrderNumberEnable: bool, openCashBoxOnGuestTickets: bool, openCashBoxOnPrechecks: bool,
                 openCashBoxOnReports: bool, printGuestTicket: bool, printKitchenTicket: bool, services: list,
                 tableScheme: dict, title: str, backupPrechecksTargetDevice: dict = None, 
                 kkmOrganization1:dict = None, kkmOrganization2: dict = None, 
                 prechecksTargetDevice: dict = None, reportTargetDevice: dict = None, **kwargs):
        class_name: str = "modules.warehouse.nomenclature.sale_place.SalePlace"

        super().__init__(class_name=class_name, **kwargs)
        self._automatic_encashment: bool = automaticEncashment
        self._can_hold_table_orders: bool = canHoldTableOrders
        self._default_cooking_place: CookingPlace = CookingPlace(**defaultCookingPlace)
        self._max_table_order_number_enable: bool = maxTableOrderNumberEnable
        self._open_cash_box_on_guest_tickets: bool = openCashBoxOnGuestTickets
        self._open_cash_box_on_prechecks: bool = openCashBoxOnPrechecks
        self._open_cash_box_on_reports: bool = openCashBoxOnReports
        self._print_guest_ticket: bool = printGuestTicket
        self._print_kitchen_ticket: bool = printKitchenTicket
        self._services: list = services
        self._title: str = title
        self._table: TableScheme = TableScheme(**tableScheme)

        self._backup_prechecks_target_device = TerminalDevice(**backupPrechecksTargetDevice)
        self._kkm_organization1 = TerminalDevice(**kkmOrganization1)
        self._kkm_organization2 = TerminalDevice(**kkmOrganization2)
        self._prechecks_target_device = TerminalDevice(**prechecksTargetDevice)
        self._report_target_device = TerminalDevice(**reportTargetDevice)