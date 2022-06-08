from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.nomenclature.cooking_place import CookingPlace


class DishSale(QuickRestoObject):
    def __init__(self, cookingPlace: dict, price:float, **kwargs):
        super().__init__(className="warehouse.nomenclature.dish.dishSale", **kwargs)
        self._cooking_place: CookingPlace = CookingPlace(**cookingPlace)
