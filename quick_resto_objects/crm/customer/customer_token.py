from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.crm.customer.token_types import *


class CustomerToken(QuickRestoObject):
    @property
    def token_type(self) -> TokenType:
        return self._token_type

    @property
    def entry(self) -> EntryType:
        return self._entry

    @property
    def key(self) -> str:
        return self._key

    def __init__(self, entry: str, key: str, type: str, **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.customer.CrmToken"

        super().__init__(class_name=class_name, **kwargs)
        self._entry: EntryType = convert_str_to_crm_entry_type(entry)
        self._key: str = key
        self._token_type: TokenType = convert_str_to_crm_token_type(type)
