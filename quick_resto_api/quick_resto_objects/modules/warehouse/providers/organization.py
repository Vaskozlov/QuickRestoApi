from quick_resto_objects.quick_resto_object import QuickRestoObject


class Organization(QuickRestoObject):
    @property
    def short_name(self) -> str:
        return self._short_name

    @property
    def address(self) -> str:
        return self._address

    @property
    def delivery_address(self) -> str:
        return self._delivery_address

    @property
    def egais_status(self) -> str:
        return self._egais_status

    @property
    def egais_activity_status(self) -> str:
        return self._egais_activity_status

    @property
    def full_name(self) -> str:
        return self._full_name

    def __init__(self, shortName: str = None, address: str = None, deliveryAddress: str = None, egaisStatus: str = None,
                 egaisActivityStatus: str = None, fullName: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.providers.Organization"

        super().__init__(class_name=class_name, **kwargs)

        self._short_name: str = shortName
        self._address: str = address
        self._delivery_address: str = deliveryAddress
        self._egais_status: str = egaisStatus
        self._egais_activity_status: str = egaisActivityStatus
        self._full_name: str = fullName
