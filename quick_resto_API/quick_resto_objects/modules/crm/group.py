from quick_resto_objects.quick_resto_object import QuickRestoObject


class Group(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def group_id(self) -> int:
        return self._group_id

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def discount_value(self) -> float:
        return self._discount_value

    @property
    def customer_operation_limit(self) -> int:
        return self._customer_operation_limit

    def __init__(self, groupId: int = None, deleted: bool = None, name: str = None, discountValue: float = None,
                 customerOperationLimit: int = None,
                 **kwargs):
        class_name = "ru.edgex.quickresto.modules.crm.customer.group.Group"

        super().__init__(class_name=class_name, **kwargs)
        self._group_id: int = groupId
        self._deleted: bool = deleted
        self._name: str = name
        self._discount_value: float = discountValue
        self._customer_operation_limit: int = customerOperationLimit
