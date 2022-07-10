from quick_resto_objects.modules.warehouse.cooking_place import CookingPlace
from quick_resto_objects.modules.warehouse.sale_place import SalePlace
from quick_resto_objects.quick_resto_object import QuickRestoObject


class DishSale(QuickRestoObject):
    def __init__(self, cookingPlace: dict = None, price: float = None, salePlace: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.warehouse.nomenclature.dish.dishSale.DishSale"

        super().__init__(class_name=class_name, **kwargs)
        self._price: float = price

        if salePlace is not None: 
            self._sale_place: SalePlace = SalePlace(**salePlace)
        else:
            self._sale_place = None

        if cookingPlace is not None: 
            self._cooking_place: CookingPlace = CookingPlace(**cookingPlace)
        else:
            self._cooking_place = None
