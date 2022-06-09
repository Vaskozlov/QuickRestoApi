from quick_resto_objects.quick_resto_object import QuickRestoObject
from quick_resto_objects.nomenclature.cooking_place import CookingPlace
from quick_resto_objects.nomenclature.sale_place import SalePlace


class DishSale(QuickRestoObject):
    def __init__(self, cookingPlace: dict, price: float, salePlace: dict, **kwargs):
        class_name = "modules.warehouse.nomenclature.dish.dishSale"
        super().__init__(class_name=class_name, **kwargs)
        self._price: float = price
        self._sale_place: SalePlace = SalePlace(**salePlace)
        self._cooking_place: CookingPlace = CookingPlace(**cookingPlace)
