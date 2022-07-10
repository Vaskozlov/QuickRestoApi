from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.alcohol.alcohol_dictionary import AlcoholDictionary

class AlcoholDictionaryOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "alcohol.dictionary"

    def get_list_of_alcohol_dictionary(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(AlcoholDictionary(**object))

        return result

    def get_tree_of_alcohol_dictionary(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(AlcoholDictionary(**object))

        return result

    def get_alcohol_dictionary(self, objectId: int, objectRid: int = None) -> AlcoholDictionary:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        return AlcoholDictionary(**json_response)

    def get_alcohol_dictionary_with_subobjects(self, objectId: int, objectRid: int = None) -> AlcoholDictionary:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        return AlcoholDictionary(**json_response)

    def create_alcohol_dictionary(self, object: AlcoholDictionary,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> AlcoholDictionary:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return AlcoholDictionary(**json_response)

    def update_alcohol_dictionary(self, object: AlcoholDictionary,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> AlcoholDictionary:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return AlcoholDictionary(**json_response)

    def remove_alcohol_dictionary(self, object: AlcoholDictionary,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> AlcoholDictionary:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return AlcoholDictionary(**json_response)

    def recover_alcohol_dictionary(self, object: AlcoholDictionary,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> AlcoholDictionary:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return AlcoholDictionary(**json_response)