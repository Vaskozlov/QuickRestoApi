from quick_resto_objects.modules.warehouse.store import Store
from quick_resto_objects.quick_resto_object import QuickRestoObject


class CookingInvoice(QuickRestoObject):
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

    def __init__(self, fromStore: dict = None, documentNumber: str = None, invoiceDate: str = None, store: dict = None,
                 processed: bool = None, totalSum: float = None,
                 totalSumWoNds: float = None, totalNds: float = None, comment: str = None, totalAmount: float = None,
                 **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.documents.cooking.CookingInvoice"

        super().__init__(class_name=class_name, **kwargs)

        if fromStore is not None: 
            self._from_store = Store(**fromStore)
        else:
            self._from_store = None

        self._document_number: str = documentNumber
        self._invoice_date: str = invoiceDate

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
