from quick_resto_objects.quick_resto_object import QuickRestoObject


class ProviderGroup(QuickRestoObject):
    @property
    def short_name(self) -> str:
        return self._short_name

    @property
    def egais_status(self) -> str:
        return self._egais_status

    @property
    def egais_activity_status(self) -> str:
        return self._egais_activity_status

    def __init__(self, shortName: str = None, egaisStatus: str = None, egaisActivityStatus: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.providers.ProviderGroup"

        super().__init__(class_name=class_name, **kwargs)

        self._short_name: str = shortName
        self._egais_status: str = egaisStatus
        self._egais_activity_status: str = egaisActivityStatus
