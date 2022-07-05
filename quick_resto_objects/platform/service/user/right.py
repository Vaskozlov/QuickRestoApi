from quick_resto_objects.quick_resto_object import QuickRestoObject


class Right(QuickRestoObject):
    @property
    def title(self) -> str:
        return self._title

    def __init__(self, title: str = None, **kwargs):
        class_name = "ru.edgex.platform.service.user.Right"

        super().__init__(class_name=class_name, **kwargs)

        self._title: str = title
