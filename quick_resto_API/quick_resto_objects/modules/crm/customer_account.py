from quick_resto_objects.modules.crm.account_type import AccountType
from quick_resto_objects.modules.crm.account_balance import AccountBalance
from quick_resto_objects.quick_resto_object import QuickRestoObject


class CustomerAccount(QuickRestoObject):
    def __init__(self, accountBalance: dict = None, accountState: bool = None, accountType: dict = None,
                 convertBonuses: bool = None, deleted: bool = None,
                 hidden: bool = None, **kwargs):
        class_name = 'ru.edgex.quickresto.modules.crm.accounting.account.CustomerAccount'

        super().__init__(id=0, class_name=class_name, **kwargs)

        if accountBalance is not None: 
            self._accounts = AccountBalance(**accountBalance)
        else:
            self._accounts = None

        self._account_state: bool = accountState

        if accountType is not None: 
            self._account_type: AccountType = AccountType(**accountType)
        else:
            self._account_type = None

        self._convert_bonuses: bool = convertBonuses
        self._deleted: bool = deleted
        self._hidden: bool = hidden
