from quick_resto_objects.modules.front.table import Table
from quick_resto_objects.modules.front.terminal import Terminal
from quick_resto_objects.modules.front.shift import Shift
from quick_resto_objects.modules.personnel.employee import Employee
from quick_resto_objects.quick_resto_object import QuickRestoObject


class OrderInfo(QuickRestoObject):
    @property
    def comment(self) -> str:
        return self._comment

    @property
    def create_date(self) -> str:
        return self._create_date

    @property
    def document_number(self) -> int:
        return self._document_number

    @property
    def discount_percent(self) -> int:
        return self._discount_percent

    @property
    def cashier(self) -> Employee:
        return self._cashier

    @property
    def ext_id(self) -> str:
        return self._ext_id

    @property
    def front(self) -> Terminal:
        return self._front

    @property
    def front_sum(self) -> int:
        return self._front_sum

    @property
    def front_total_absolute_charge(self) -> int:
        return self._front_total_absolute_charge

    @property
    def front_total_absolute_discount(self) -> int:
        return self._front_total_absolute_discount

    @property
    def front_total_bonuses(self) -> int:
        return self._front_total_bonuses

    @property
    def front_total_card(self) -> int:
        return self._front_total_card

    @property
    def front_total_cash_minus_discount(self) -> int:
        return self._front_total_cash_minus_discount

    @property
    def front_total_discount(self) -> int:
        return self._front_total_discount

    @property
    def front_total_price(self) -> int:
        return self._front_total_price

    @property
    def kkm_terminal_name(self) -> str:
        return self._kkm_terminal_name

    @property
    def original_order_doc_id(self) -> str:
        return self._original_order_doc_id

    @property
    def precheck_doc_id(self) -> str:
        return self._precheck_doc_id

    @property
    def reopened_order_doc_id(self) -> str:
        return self._reopened_order_doc_id

    @property
    def returned(self) -> bool:
        return self._returned

    @property
    def return_order_doc_id(self) -> str:
        return self._return_order_doc_id

    @property
    def shift(self) -> Shift:
        return self._shift

    @property
    def shift_id(self) -> str:
        return self._shift_id

    @property
    def table(self) -> Table:
        return self._table

    @property
    def table_order_doc_id(self) -> str:
        return self._table_order_doc_id

    @property
    def total_sum(self) -> int:
        return self._total_sum

    @property
    def waiter(self) -> Employee:
        return self._waiter

    def __init__(self, comment: str = None, createDate: str = None, documentNumber: int = None,
                 discountPercent: int = None, cashier: dict = None, extId: str = None,
                 front: dict = None, frontSum: int = None, frontTotalAbsoluteCharge: int = None,
                 frontTotalAbsoluteDiscount: int = None, frontTotalBonuses: int = None,
                 frontTotalCard: int = None, frontTotalCashMinusDiscount: int = None, frontTotalDiscount: int = None,
                 frontTotalPrice: int = None,
                 kkmTerminalName: str = None, originalOrderDocId: str = None, precheckDocId: str = None,
                 reopenedOrderDocId: str = None, returned: bool = None,
                 returnOrderDocId: str = None, shift: dict = None, shiftId: str = None, table: dict = None,
                 tableOrderDocId: str = None, totalSum: int = None,
                 waiter: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.orders.OrderInfo"

        super().__init__(class_name=class_name, **kwargs)

        self._comment: str = comment
        self._create_date: str = createDate
        self._document_number: int = documentNumber
        self._discount_percent: int = discountPercent
        
        if cashier is not None: 
            self._cashier = Employee(**cashier)
        else:
            self._cashier = None
        
        self._ext_id: str = extId

        if front is not None: 
            self._front = Terminal(**front)
        else:
            self._front = None

        self._front_sum: int = frontSum
        self._front_total_absolute_charge: int = frontTotalAbsoluteCharge
        self._front_total_absolute_discount: int = frontTotalAbsoluteDiscount
        self._front_total_bonuses: int = frontTotalBonuses
        self._front_total_card: int = frontTotalCard
        self._front_total_cash_minus_discount: int = frontTotalCashMinusDiscount
        self._front_total_discount: int = frontTotalDiscount
        self._front_total_price: int = frontTotalPrice
        self._kkm_terminal_name: str = kkmTerminalName
        self._original_order_doc_id: str = originalOrderDocId
        self._precheck_doc_id: str = precheckDocId
        self._reopened_order_doc_id: str = reopenedOrderDocId
        self._returned: bool = returned
        self._return_order_doc_id: str = returnOrderDocId

        if shift is not None: 
            self._shift = Shift(**shift)
        else:
            self._shift = None

        self._shift_id: str = shiftId
        
        if table is not None: 
            self._table = Table(**table)
        else:
            self._table = None

        self._table_order_doc_id: str = tableOrderDocId
        self._total_sum: int = totalSum

        if waiter is not None: 
            self._waiter = Employee(**waiter)
        else:
            self._waiter = None
