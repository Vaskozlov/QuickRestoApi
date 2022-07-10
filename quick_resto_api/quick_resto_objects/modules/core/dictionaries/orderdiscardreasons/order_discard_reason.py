from enum import Enum

from quick_resto_objects.quick_resto_object import QuickRestoObject


class SystemOrderDiscardReason(Enum):
    CancellationOfWriteOff = "CancellationOfWriteOff",
    CancellationWithoutWriteOffs = "CancellationWithoutWriteOffs",
    NONE = "NONE"


StrToSystemOrderDiscardReason = {
    SystemOrderDiscardReason.CancellationOfWriteOff.value: SystemOrderDiscardReason.CancellationOfWriteOff,
    SystemOrderDiscardReason.CancellationWithoutWriteOffs.value: SystemOrderDiscardReason.CancellationWithoutWriteOffs,
    SystemOrderDiscardReason.NONE.value: SystemOrderDiscardReason.NONE
}


def convert_str_to_system_order_discard_reason(value: str) -> SystemOrderDiscardReason:
    if value in SystemOrderDiscardReason.keys():
        return StrToSystemOrderDiscardReason[value]

    return SystemOrderDiscardReason.NONE


class OrderDiscardReason(QuickRestoObject):
    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def save_to_terminals(self) -> bool:
        return self._save_to_terminals

    @property
    def title(self) -> str:
        return self._title

    @property
    def use_comment(self) -> bool:
        return self._use_comment

    @property
    def withdraw_from_store(self) -> bool:
        return self._withdraw_from_store

    @property
    def system_order_discard_reason(self) -> SystemOrderDiscardReason:
        return self._system_order_discard_reason

    def __init__(self, saveToTerminals: bool = None, systemOrderDiscardReason: str = None, title: str = None,
                 useComment: bool = None,
                 withdrawFromStore: bool = None, deleted: bool = None, **kwargs):
        class_name: str = "ru.edgex.quickresto.modules.core.dictionaries.orderdiscardreasons.OrderDiscardReason"

        super().__init__(class_name=class_name, **kwargs)

        self._deleted = deleted
        self._save_to_terminals = saveToTerminals
        self._title = title
        self._use_comment = useComment
        self._withdraw_from_store = withdrawFromStore
        self._system_order_discard_reason = convert_str_to_system_order_discard_reason(systemOrderDiscardReason)
