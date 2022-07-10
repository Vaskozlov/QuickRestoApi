from datetime import date

from quick_resto_objects.modules.front.table import Table
from quick_resto_objects.quick_resto_object import QuickRestoObject


class PreorderInfo(QuickRestoObject):
    @property
    def cancellation_reason_comment(self) -> str:
        return self._cancellation_reason_comment

    @property
    def create_date(self) -> date:
        return self._create_date

    @property
    def discount_percent(self) -> int:
        return self._discount_percent

    @property
    def front_total_absolute_charge(self) -> int:
        return self._front_total_absolute_charge

    @property
    def front_total_absolute_discount(self) -> int:
        return self._front_total_absolute_discount

    @property
    def front_total_discount(self) -> int:
        return self._front_total_discount

    @property
    def guest_count(self) -> int:
        return self._guest_count

    @property
    def print_time(self) -> int:
        return self._print_time

    @property
    def sum(self) -> int:
        return self._sum

    @property
    def sum_with_discount(self) -> int:
        return self._sum_with_discount

    @property
    def table(self) -> Table:
        return self._table

    @property
    def table_order_doc_id(self) -> str:
        return self._table_order_doc_id

    def __init__(self, cancellationReasonComment: str = None, createDate: date = None, discountPercent: int = None,
                 frontTotalAbsoluteCharge: int = None,
                 frontTotalAbsoluteDiscount: int = None, frontTotalDiscount: int = None, guestCount: int = None,
                 printTime: int = None, sum: int = None,
                 sumWithDiscount: int = None, table: dict = None, tableOrderDocId: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.preorders.PreorderInfo"

        super().__init__(class_name=class_name, **kwargs)

        self._cancellation_reason_comment: str = cancellationReasonComment
        self._create_date = createDate
        self._discount_percent: int = discountPercent
        self._front_total_absolute_charge: int = frontTotalAbsoluteCharge
        self._front_total_absolute_discount: int = frontTotalAbsoluteDiscount
        self._front_total_discount: int = frontTotalDiscount
        self._guest_count: int = guestCount
        self._print_time: int = printTime
        self._sum: int = sum
        self._sum_with_discount: int = sumWithDiscount

        if table is not None: 
            self._table = Table(**table)
        else:
            self._table = None
            
        self._table_order_doc_id: str = tableOrderDocId
