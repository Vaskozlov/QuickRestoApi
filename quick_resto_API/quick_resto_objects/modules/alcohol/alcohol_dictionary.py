from quick_resto_objects.modules.warehouse.dish import Dish
from quick_resto_objects.quick_resto_object import QuickRestoObject

class AlcoholDictionary(QuickRestoObject):
    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def egais_name(self) -> str:
        return self._egais_name

    @property
    def egais_size(self) -> int:
        return self._egais_size

    @property
    def egais_type_code(self) -> str:
        return self._egais_type_code

    @property
    def show_on_terminal(self) -> bool:
        return self._show_on_terminal

    @property
    def store_product(self) -> Dish:
        return self._store_product

    def __init__(self, deleted: bool = None, egaisName: str = None, egaisSize: int = None, egaisTypeCode: str = None,
                 showOnTerminal: bool = None, storeProduct: dict = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.alcohol.dictionary.AlcoholDictionary"

        super().__init__(class_name=class_name, **kwargs)

        self._deleted: bool = deleted
        self._egais_name: str = egaisName
        self._egais_size: int = egaisSize
        self._egais_type_code: str = egaisTypeCode
        self._show_on_terminal: bool = showOnTerminal

        if storeProduct is not None:
            self._store_product = Dish(**storeProduct)
        else:
            self._store_product = None
