from enum import Enum

from quick_resto_objects.modules.crm.contact_method import ContactMethod
from quick_resto_objects.modules.crm.customer_account import CustomerAccount
from quick_resto_objects.modules.crm.customer_token import CustomerToken
from quick_resto_objects.modules.crm.group import Group
from quick_resto_objects.quick_resto_object import QuickRestoObject


class CrmCustomerType(Enum):
    NONE = "NONE"
    CUSTOMER = 'customer'


class CrmCustomerSex(Enum):
    NONE = "NONE"
    MALE = "male"
    FEMALE = "female"


StrToCrmCustomerType = {
    CrmCustomerType.CUSTOMER.value: CrmCustomerType.CUSTOMER
}

StrToCrmCustomerSex = {
    CrmCustomerSex.MALE.value: CrmCustomerSex.MALE,
    CrmCustomerSex.FEMALE.value: CrmCustomerSex.FEMALE
}


def convert_str_to_crm_customer_type(crm_customer_type: str) -> CrmCustomerType:
    crm_customer_type = crm_customer_type.upper()

    if crm_customer_type in CrmCustomerType.__members__.keys():
        return CrmCustomerType.__members__[crm_customer_type]

    return CrmCustomerType.NONE


def convert_str_to_crm_customer_sex(crm_customer_sex: str) -> CrmCustomerSex:
    crm_customer_sex = crm_customer_sex.upper()

    if crm_customer_sex in CrmCustomerSex.__members__.keys():
        return CrmCustomerSex.__members__[crm_customer_sex]

    return CrmCustomerSex.NONE


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
    def middle_name(self) -> str:
        return self._middle_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def sex(self) -> CrmCustomerSex:
        return self._sex

    @property
    def tokens(self) -> list:
        return self._tokens

    @property
    def comment(self) -> str:
        return self._comment

    @property
    def date_of_birth(self) -> str:
        return self._date_of_birth

    @property
    def customer_type(self) -> CrmCustomerType:
        return self._customer_type

    def __init__(self, accounts: list = None, addresses: list = None, contactMethods: list = None,
                 customerGuid: str = None,
                 firstName: str = None, lastName: str = None, tokens: list = None, type: str = None,
                 customerGroup: dict = None, comment: str = "",
                 middleName: str = "", sex: str = "", dateOfBirth: str = "", **kwargs):
        class_name: str = 'ru.edgex.quickresto.modules.crm.customer.CrmCustomer'

        super().__init__(class_name=class_name, **kwargs)
        if (accounts != None): self._accounts: list = [CustomerAccount(**account) for account in accounts]
        self._addresses: list = addresses
        if (contactMethods != None): self._contact_methods: list = [ContactMethod(**contact_method) for contact_method
                                                                    in contactMethods]
        self._customer_guid: str = customerGuid
        self._first_name: str = firstName
        self._middle_name: str = middleName
        self._last_name: str = lastName
        self._sex: CrmCustomerSex = convert_str_to_crm_customer_sex(sex)
        self._comment: str = comment
        self._date_of_birth: str = dateOfBirth

        if tokens is not None: 
            self._tokens: list = [CustomerToken(**token) for token in tokens]
        else:
            self._tokens = None

        self._customer_type: CrmCustomerType = convert_str_to_crm_customer_type(type)

        if customerGroup is None: 
            self._group: Group = Group(**customerGroup)
        else:
            self._group = None
