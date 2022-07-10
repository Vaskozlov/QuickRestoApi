from quick_resto_objects.quick_resto_object import QuickRestoObject


class Employee(QuickRestoObject):
    @property
    def system_employee(self) -> str:
        return self._system_employee

    @property
    def user(self) -> dict:
        return self._user

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def blocked(self) -> bool:
        return self._blocked

    @property
    def short_name(self) -> str:
        return self._short_name

    @property
    def full_name(self) -> str:
        return self._full_name

    def __init__(self, systemEmployee: str = None, user: dict = None, firstName: str = None, lastName: str = None,
                 blocked: bool = None,
                 shortName: str = None, fullName: str = None, **kwargs):
        class_name = ""
        super().__init__(class_name=class_name, **kwargs)

        self._system_employee: str = systemEmployee
        self._user: dict = user
        self._first_name: str = firstName
        self._last_name: str = lastName
        self._blocked: bool = blocked
        self._short_name: str = shortName
        self._full_name: str = fullName
