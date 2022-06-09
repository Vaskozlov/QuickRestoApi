from enum import Enum
from quick_resto_objects.quick_resto_object import QuickRestoObject


class CustomerToken(QuickRestoObject):
    def __int__(self, **kwargs):
        class_name: str = 'ru.edgex.quickresto.modules.crm.customer.CrmCustomerToken'

        super().__init__(class_name=class_name, **kwargs)
