from quick_resto_objects.modules.warehouse.nomenclature.cooking_place.cooking_place import CookingPlace
from quick_resto_objects.modules.warehouse.nomenclature.sale_place.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class DishSale(QuickRestoObject):
    def __init__(self, cookingPlace: dict=None, price: float=None, salePlace: dict=None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.dish.dishSale.DishSale"

        super().__init__(class_name=class_name, **kwargs)
        self._price: float = price
        if (salePlace!=None):self._sale_place: SalePlace = SalePlace(**salePlace)
        if (cookingPlace!=None):self._cooking_place: CookingPlace = CookingPlace(**cookingPlace)