from quick_resto_objects.quick_resto_object import QuickRestoObject


class CookingPlace(QuickRestoObject):
    def __init__(self, sendSignal: bool, **kwargs):
        super().__init__(**kwargs)
        self._send_signal = sendSignal

