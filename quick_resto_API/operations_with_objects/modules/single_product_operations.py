from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.warehouse.single_category import SingleCategory
from quick_resto_objects.modules.warehouse.single_product import SingleProduct

class SingleProductOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "warehouse.nomenclature.singleproduct"
    
    def get_list_of_single_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'SingleCategory' in object['className']:
                result.append(SingleCategory(**object))
            elif 'SingleProduct' in object['className']:
                result.append(SingleProduct(**object))

        return result

    def get_tree_of_single_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'SingleCategory' in object['className']:
                result.append(SingleCategory(**object))
            elif 'SingleProduct' in object['className']:
                result.append(SingleProduct(**object))

        return result

    def get_single_product_or_single_category(self, objectId: int, objectRid: int = None) -> SingleProduct | SingleCategory:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def get_single_product_or_single_category_with_subobjects(self, objectId: int, objectRid: int = None) -> SingleProduct | SingleCategory:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def create_single_product_or_single_category(self, object: SingleProduct | SingleCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def update_single_product_or_single_category(self, object: SingleProduct | SingleCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def remove_single_product_or_single_category(self, object: SingleProduct | SingleCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def recover_single_product_or_single_category(self, object: SingleProduct | SingleCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)