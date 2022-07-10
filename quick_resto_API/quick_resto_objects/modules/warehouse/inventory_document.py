from quick_resto_objects.modules.warehouse.store import Store
from quick_resto_objects.quick_resto_object import QuickRestoObject


class InventoryDocument(QuickRestoObject):
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
    def shortfall_sum(self) -> float:
        return self._shortfall_sum

    @property
    def surplus_sum(self) -> float:
        return self._surplus_sum

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def total_amount(self) -> float:
        return self._total_amount

    def __init__(self, documentNumber: str = None, invoiceDate: str = None, store: dict = None, processed: bool = None,
                 totalSum: float = None, totalSumWoNds: float = None,
                 totalNds: float = None, shortfallSum: float = None, surplusSum: float = None, comment: str = None,
                 totalAmount: float = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.inventory.document.InventoryDocument"

        super().__init__(class_name=class_name, **kwargs)

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
        self._shortfall_sum: float = shortfallSum
        self._surplus_sum: float = surplusSum
        self._comment: str = comment
        self._total_amount: float = totalAmount
