from quick_resto_objects.quick_resto_object import QuickRestoObject


class AccountType(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def account_guid(self) -> str:
        return self._account_guid

    @property
    def deleted(self) -> float:
        return self._deleted

    @property
    def max_usage(self) -> float:
        return self._max_usage

    @property
    def reset_period(self) -> float:
        return self._reset_period

    def __init__(self, accountGuid: str = None, deleted: bool = None, maxUsage: float = None, name: str = None,
                 resetPeriod: float = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.accounting.account.account_balance.AccountType"

        super().__init__(id=0, class_name=class_name, **kwargs)
        self._name: str = name
        self._account_guid: str = accountGuid
        self._deleted: bool = deleted
        self._max_usage: float = maxUsage
        self._reset_period: float = resetPeriod
