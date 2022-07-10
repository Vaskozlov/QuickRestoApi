from quick_resto_objects.quick_resto_object import QuickRestoObject


class Businessman(QuickRestoObject):
    @property
    def short_name(self) -> str:
        return self._short_name

    @property
    def egais_status(self) -> str:
        return self._egais_status

    @property
    def egais_activity_status(self) -> str:
        return self._egais_activity_status

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def middle_name(self) -> str:
        return self._middle_name

    @property
    def last_name(self) -> str:
        return self._last_name

    def __init__(self, shortName: str = None, egaisStatus: str = None, egaisActivityStatus: str = None,
                 firstName: str = None,
                 middleName: str = None, lastName: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.providers.Businessman"

        super().__init__(class_name=class_name, **kwargs)

        self._short_name: str = shortName
        self._egais_status: str = egaisStatus
        self._egais_activity_status: str = egaisActivityStatus
        self._first_name: str = firstName
        self._middle_name: str = middleName
        self._last_name: str = lastName
