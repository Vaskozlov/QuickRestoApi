from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.crm.fixed_discount import FixedDiscount

class FixedDiscountOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "crm.settings.fixed"

    def get_list_of_fixed_discount(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(FixedDiscount(**object))

        return result

    def get_tree_of_fixed_discount(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(FixedDiscount(**object))

        return result

    def get_fixed_discount(self, objectId: int, objectRid: int = None) -> FixedDiscount:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        return FixedDiscount(**json_response)

    def get_fixed_discount_with_subobjects(self, objectId: int, objectRid: int = None) -> FixedDiscount:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        return FixedDiscount(**json_response)

    def create_fixed_discount(self, object: FixedDiscount,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> FixedDiscount:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return FixedDiscount(**json_response)

    def update_fixed_discount(self, object: FixedDiscount,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> FixedDiscount:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return FixedDiscount(**json_response)

    def remove_fixed_discount(self, object: FixedDiscount,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> FixedDiscount:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return FixedDiscount(**json_response)

    def recover_fixed_discount(self, object: FixedDiscount,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> FixedDiscount:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return FixedDiscount(**json_response)