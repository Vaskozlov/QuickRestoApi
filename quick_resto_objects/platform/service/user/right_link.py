from quick_resto_objects.platform.service.user.right import Right
from quick_resto_objects.quick_resto_object import QuickRestoObject

class RightLink(QuickRestoObject):
    @property
    def right(self) -> Right:
        return self._right

    def __init__(self, right: dict, **kwargs):
        class_name = "ru.edgex.platform.service.user.RightLink"

        super().__init__(class_name=class_name, **kwargs)

        self._right: dict = Right(**right)