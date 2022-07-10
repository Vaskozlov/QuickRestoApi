from quick_resto_objects.modules.warehouse.businessman import Businessman
from quick_resto_objects.modules.warehouse.natural_person import NaturalPerson
from quick_resto_objects.modules.warehouse.organization import Organization
from quick_resto_objects.modules.warehouse.provider_group import ProviderGroup
from quick_resto_objects.modules.warehouse.store import Store
from quick_resto_objects.quick_resto_object import QuickRestoObject


class IncomingInvoice(QuickRestoObject):
    @property
    def document_number(self) -> str:
        return self._document_number

    @property
    def invoice_date(self) -> str:
        return self._invoice_date

    @property
    def provider(self) -> QuickRestoObject:
        return self._provider

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
    def paid(self) -> bool:
        return self._paid

    @property
    def total_amount(self) -> float:
        return self._total_amount

    def __init__(self, documentNumber: str, invoiceDate: str, processed: bool, totalSum: float, totalSumWoNds: float,
                 totalNds: float, paid: bool, totalAmount: float, provider: dict = None, store: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.documents.incoming.IncomingInvoice"

        super().__init__(class_name=class_name, **kwargs)

        self._paid = paid
        self._document_number = documentNumber
        self._invoice_date = invoiceDate
        self._processed = processed
        self._total_sum = totalSum
        self._total_sum_wo_nds = totalSumWoNds
        self._total_nds = totalNds
        self._total_amount = totalAmount

        if store is not None:
            self._store = Store(**store)

        if provider is not None:
            if provider is Businessman:
                self._provider = Businessman(**provider)
            elif provider is NaturalPerson:
                self._provider = NaturalPerson(**provider)
            elif provider is Organization:
                self._provider = Organization
            elif provider is ProviderGroup:
                self._provider = ProviderGroup(**provider)
            else:
                provider = None
        else:
                provider = None
