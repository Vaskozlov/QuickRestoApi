from quick_resto_objects.quick_resto_object import QuickRestoObject


class StoreItemTag(QuickRestoObject):
    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def name(self) -> str:
        return self._name

    def __init__(self, name: str = None, deleted: bool = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.core.dictionaries.storeitemtag.StoreItemTag"

        super().__init__(class_name=class_name, **kwargs)

        self._deleted = deleted
        self._name = name
