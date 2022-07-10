from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.warehouse.semi_product import SemiProduct
from quick_resto_objects.modules.warehouse.store_category import StoreCategory

class SemiProductOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "warehouse.nomenclature.semiproduct"

    def get_list_of_semi_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'StoreCategory' in object['className']:
                result.append(StoreCategory(**object))
            elif 'SemiProduct' in object['className']:
                result.append(SemiProduct(**object))

        return result

    def get_tree_of_semi_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'StoreCategory' in object['className']:
                result.append(StoreCategory(**object))
            elif 'SemiProduct' in object['className']:
                result.append(SemiProduct(**object))

        return result

    def get_semi_product_or_store_category(self, objectId: int, objectRid: int = None) -> SemiProduct | StoreCategory:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def get_semi_product_or_store_category_with_subobjects(self, objectId: int, objectRid: int = None) -> SemiProduct | StoreCategory:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def create_semi_product_or_store_category(self, object: SemiProduct | StoreCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def update_semi_product_or_store_category(self, object: SemiProduct | StoreCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def remove_semi_product_or_store_category(self, object: SemiProduct | StoreCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def recover_semi_product_or_store_category(self, object: SemiProduct | StoreCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)