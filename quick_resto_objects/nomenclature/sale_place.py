from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.nomenclature.cooking_place import CookingPlace
from quick_resto_objects.tablemanagement.table_scheme import TableScheme


class SalePlace(QuickRestoObject):
    def __init__(self, automaticEncashment: bool, canHoldTableOrders: bool, defaultCookingPlace: dict,
                 maxTableOrderNumberEnable: bool, openCashBoxOnGuestTickets: bool, openCashBoxOnPrechecks: bool,
                 openCashBoxOnReports: bool, printGuestTicket: bool, printKitchenTicket: bool, services: list,
                 tableScheme: dict, title: str, **kwargs):
        class_name: str = "modules.warehouse.nomenclature.salePlace"

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
