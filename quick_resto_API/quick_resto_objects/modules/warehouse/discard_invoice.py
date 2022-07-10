from quick_resto_objects.modules.warehouse.outgoing_invoice import convert_str_to_customer_type, CustomerType
from quick_resto_objects.modules.warehouse.store import Store
from quick_resto_objects.quick_resto_object import QuickRestoObject


class DiscardInvoice(QuickRestoObject):
    @property
    def document_number(self) -> str:
        return self._document_number

    @property
    def invoice_date(self) -> str:
        return self._invoice_date

    @property
    def customer_type(self) -> CustomerType:
        return self._customer_type

    @property
    def store(self) -> Store:
        return self._store

    @property
    def processed(self) -> bool:
        return self._processed

    @property
    def total_sum(self) -> float:
        return self._total_sum

    @property
    def total_sum_wo_nds(self) -> float:
        return self._total_sum_wo_nds

    @property
    def total_nds(self) -> float:
        return self._total_nds

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def total_amount(self) -> float:
        return self._total_amount

    @property
    def discard_reason(self) -> dict:
        return self._discard_reason

    @property
    def subject(self) -> dict:
        return self._subject

    @property
    def operator(self) -> dict:
        return self._operator

    @property
    def guest(self) -> dict:
        return self._guest

    def __init__(self, documentNumber: str = None, invoiceDate: str = None, customerType: str = None,
                 store: dict = None, processed: bool = None, totalSum: float = None,
                 totalSumWoNds: float = None, totalNds: float = None, comment: str = None, totalAmount: float = None,
                 discardReason: dict = None,
                 subject: dict = None, operator: dict = None, guest: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.documents.discard.DiscardInvoice"

        super().__init__(class_name=class_name, **kwargs)

        self._document_number: str = documentNumber
        self._invoice_date: str = invoiceDate
        self._customer_type = convert_str_to_customer_type(customerType)

        if store is not None: 
            self._store = Store(**store)
        else:
            self._store = None

        self._processed: bool = processed
        self._total_sum: float = totalSum
        self._total_sum_wo_nds: float = totalSumWoNds
        self._total_nds: float = totalNds
        self._comment: str = comment
        self._total_amount: float = totalAmount

        self._discard_reason: dict = discardReason
        self._subject: dict = subject
        self._operator: dict = operator
        self._guest: dict = guest
