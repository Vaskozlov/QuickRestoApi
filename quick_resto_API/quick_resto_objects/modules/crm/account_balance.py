from quick_resto_objects.quick_resto_object import QuickRestoObject


class AccountBalance(QuickRestoObject):
    @property
    def available(self) -> float:
        return self._available

    @property
    def credit_hold(self) -> float:
        return self._credit_hold

    @property
    def debit_hold(self) -> float:
        return self._debit_hold

    @property
    def ledger(self) -> float:
        return self._ledger

    def __init__(self, available: float = None, creditHold: float = None, debitHold: float = None, ledger: float = None,
                 **kwargs):
        class_name = 'ru.edgex .quickresto.modules.crm.accounting.account.balance.AccountBalance'

        super().__init__(id=0, class_name=class_name, **kwargs)
        self._available: float = available
        self._credit_hold: float = creditHold
        self._debit_hold: float = debitHold
        self._ledger: float = ledger
