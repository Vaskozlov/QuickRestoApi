from quick_resto_objects.modules.warehouse.nomenclature.cooking_place.cooking_place import CookingPlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class Terminal(QuickRestoObject):
    def cooking_place(self) -> CookingPlace:
        return self._cooking_place

    def deleted(self):
        return self._deleted