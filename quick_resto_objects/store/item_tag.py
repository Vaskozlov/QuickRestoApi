from quick_resto_objects.quick_resto_object import QuickRestoObject


class ItemTag(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    def __init__(self, name: str, **kwargs):
        class_name = "ru.edgex.quickresto.modules.store.ItemTag"

        super().__init__(class_name=class_name, **kwargs)
        self._name: str = name
