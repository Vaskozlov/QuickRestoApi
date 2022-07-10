from quick_resto_objects.modules.warehouse.store import Store
from quick_resto_objects.quick_resto_object import QuickRestoObject


class ExchangeInvoice(QuickRestoObject):
    @property
    def from_store(self) -> Store:
        return self._from_store

    @property
    def document_number(self) -> str:
        return self._document_number

    @property
    def invoice_date(self) -> str:
        return self._invoice_date

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

    def __init__(self, documentNumber: str, invoiceDate: str, processed: bool, totalSum: float, totalSumWoNds: float,
                 totalNds: float, comment: str, totalAmount: float, fromStore: dict = None, store: dict = None,
                 **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.documents.exchange.ExchangeInvoice"

        super().__init__(class_name=class_name, **kwargs)

        self._document_number = documentNumber
        self._invoice_date = invoiceDate
        self._processed = processed
        self._total_sum = totalSum
        self._total_sum_wo_nds = totalSumWoNds
        self._total_nds = totalNds
        self._comment = comment
        self._total_amount = totalAmount

        if fromStore is not None: 
            self._from_store = Store(**fromStore)
        else:
            self._from_store = None

        if store is not None: 
            self._store = Store(**store)
        else:
            self._store = None
