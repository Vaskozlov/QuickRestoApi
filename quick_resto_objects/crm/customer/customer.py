from enum import Enum
from quick_resto_objects.crm.accounting.account.customer_account import *
from quick_resto_objects.crm.customer.customer_token import CustomerToken
from quick_resto_objects.crm.accounting.account.contact_method import ContactMethod


class CrmCustomerType(Enum):
    NONE = "NONE"
    CUSTOMER = 'customer'


StrToCrmCustomerType = {
    CrmCustomerType.CUSTOMER.value: CrmCustomerType.CUSTOMER
}


def convert_str_to_crm_customer_type(crm_customer_type: str) -> CrmCustomerType:
    if crm_customer_type in StrToCrmCustomerType.keys():
        return StrToCrmCustomerType[crm_customer_type]

    return CrmCustomerType.NONE


class CrmCustomer(QuickRestoObject):
    @property
    def accounts(self) -> list:
        return self._accounts

    @property
    def addresses(self) -> list:
        return self._addresses

    @property
    def contact_methods(self) -> list:
        return self._contact_methods

    @property
    def customer_guid(self) -> str:
        return self._customer_guid

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def tokens(self) -> list:
        return self._tokens

    @property
    def customer_type(self) -> CrmCustomerType:
        return self._customer_type

    def __init__(self, accounts: list, addresses: list, contactMethods: list, customerGuid: str,
                 firstName: str, lastName: str, tokens: list, type: str, **kwargs):
        class_name: str = 'ru.edgex.quickresto.modules.crm.customer.CrmCustomer'

        super().__init__(class_name=class_name, **kwargs)
        self._accounts: list = [CustomerAccount(**account) for account in accounts]
        self._addresses: list = addresses
        self._contact_methods: list = [ContactMethod(**contact_method) for contact_method in contactMethods]
        self._customer_guid: str = customerGuid
        self._first_name: str = firstName
        self._last_name: str = lastName
        self._tokens: list = tokens  # [CustomerToken(**token) for token in tokens]
        self._customer_type: CrmCustomerType = convert_str_to_crm_customer_type(type)
