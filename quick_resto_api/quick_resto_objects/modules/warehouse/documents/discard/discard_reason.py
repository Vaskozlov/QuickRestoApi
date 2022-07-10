from quick_resto_objects.quick_resto_object import QuickRestoObject


class DiscardReason(QuickRestoObject):
    @property
    def system_order_discard_reason(self) -> str:
        return self._system_order_discard_reason

    @property
    def version(self) -> int:
        return self._version

    @property
    def ref_id(self) -> str:
        return self._ref_id

    @property
    def withdraw_from_store(self) -> bool:
        return self._withdraw_from_store

    @property
    def use_comment(self) -> bool:
        return self._use_comment

    @property
    def save_to_terminals(self) -> bool:
        return self._save_to_terminals

    @property
    def description(self) -> str:
        return self._description

    def __init__(self, systemOrderDiscardReason: str = None, version: int = None, refId: str = None,
                 withdrawFromStore: bool = None,
                 useComment: bool = None, saveToTerminals: bool = None, description: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.documents.discard"

        super().__init__(class_name=class_name, **kwargs)

        self._system_order_discard_reason: str = systemOrderDiscardReason
        self._version: int = version
        self._ref_id: str = refId
        self._withdraw_from_store: bool = withdrawFromStore
        self._use_comment: bool = useComment
        self._save_to_terminals: bool = saveToTerminals
        self._description: str = description
