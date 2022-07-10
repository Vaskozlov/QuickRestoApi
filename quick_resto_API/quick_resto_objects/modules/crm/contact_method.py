from enum import Enum

from quick_resto_objects.quick_resto_object import QuickRestoObject


class ContactMethodType(Enum):
    NONE = 'NONE'
    EMAIL = 'eMail'
    PHONE = 'phoneNumber'


StrToContactMethodType = {
    ContactMethodType.EMAIL.value: ContactMethodType.EMAIL,
    ContactMethodType.PHONE.value: ContactMethodType.PHONE
}


def convert_str_to_contact_method_type(method_type: str) -> ContactMethodType:
    if method_type in StrToContactMethodType.keys():
        return StrToContactMethodType[method_type]

    return ContactMethodType.NONE


class ContactMethod(QuickRestoObject):
    @property
    def value(self) -> str:
        return self._value

    @property
    def contact_type(self) -> ContactMethodType:
        return self._contact_type

    def __init__(self, type: str = None, value: str = None, **kwargs):
        class_name: str = 'modules.crm.accounting.account.contact_method'

        super().__init__(id=0, class_name=class_name, **kwargs)
        self._value: str = value
        self._contact_type: ContactMethodType = convert_str_to_contact_method_type(type)
