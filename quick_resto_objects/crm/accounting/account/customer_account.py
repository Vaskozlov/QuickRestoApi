from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.crm.accounting.account.account_type import AccountType
from quick_resto_objects.crm.accounting.account.account_balance import AccountBalance


class CustomerAccount(QuickRestoObject):
    def __init__(self, accountBalance: dict, accountState: bool, accountType: dict, convertBonuses: bool, deleted: bool,
                 hidden: bool, **kwargs):
        class_name = 'modules.crm.accounting.account.CustomerAccount'

        super().__init__(id=0, class_name=class_name, **kwargs)
        self._accounts = AccountBalance(**accountBalance)
        self._account_state: bool = accountState
        self._account_type: AccountType = AccountType(**accountType)
        self._convert_bonuses: bool = convertBonuses
        self._deleted: bool = deleted
        self._hidden: bool = hidden
