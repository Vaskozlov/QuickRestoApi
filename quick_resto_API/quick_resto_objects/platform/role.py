from quick_resto_objects.platform.right_link import RightLink
from quick_resto_objects.quick_resto_object import QuickRestoObject


class Role(QuickRestoObject):
    @property
    def system_role(self) -> str:
        return self._system_role

    @property
    def title(self) -> str:
        return self._title

    @property
    def back_office_user(self) -> bool:
        return self._back_office_user

    @property
    def front_office_user(self) -> bool:
        return self._front_office_user

    @property
    def courier_user(self) -> bool:
        return self._courier_user

    @property
    def right_links(self) -> list:
        return self._right_links

    def __init__(self, systemRole: str = None, title: str = None, backOfficeUser: bool = None,
                 frontOfficeUser: bool = None, courierUser: bool = None,
                 rightLinks: list = None, **kwargs):
        class_name = "ru.edgex.platform.service.user.Role"

        super().__init__(class_name=class_name, **kwargs)

        self._system_role: str = systemRole
        self._title: str = title
        self._back_office_user: bool = backOfficeUser
        self._front_office_user: bool = frontOfficeUser
        self._courier_user: bool = courierUser

        if rightLinks is not None: 
            self._right_links: list = [RightLink(**value) for value in rightLinks]
        else:
            self._right_links = None
