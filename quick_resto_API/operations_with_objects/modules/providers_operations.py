from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.warehouse.businessman import Businessman
from quick_resto_objects.modules.warehouse.natural_person import NaturalPerson
from quick_resto_objects.modules.warehouse.organization import Organization
from quick_resto_objects.modules.warehouse.provider_group import ProviderGroup

class ProvidersOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "warehouse.providers"

    def get_list_of_provider(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'Businessman' in object['className']:
                result.append(Businessman(**object))
            elif 'NaturalPerson' in object['className']:
                result.append(NaturalPerson(**object))
            elif 'Organization' in object['className']:
                result.append(Organization(**object))
            elif 'ProviderGroup' in object['className']:
                result.append(ProviderGroup(**object))

        return result

    def get_tree_of_provider(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'Businessman' in object['className']:
                result.append(Businessman(**object))
            elif 'NaturalPerson' in object['className']:
                result.append(NaturalPerson(**object))
            elif 'Organization' in object['className']:
                result.append(Organization(**object))
            elif 'ProviderGroup' in object['className']:
                result.append(ProviderGroup(**object))

        return result

    def get_provider(self, objectId: int, objectRid: int = None) -> Businessman|NaturalPerson|Organization|ProviderGroup:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        if 'Businessman' in object['className']:
            return Businessman(**json_response)
        elif 'NaturalPerson' in object['className']:
            return NaturalPerson(**json_response)
        elif 'Organization' in object['className']:
            return Organization(**json_response)
        else:
            return ProviderGroup(**json_response)

    def get_provider_with_subobjects(self, objectId: int, objectRid: int = None) -> Businessman|NaturalPerson|Organization|ProviderGroup:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        if 'Businessman' in object['className']:
            return Businessman(**json_response)
        elif 'NaturalPerson' in object['className']:
            return NaturalPerson(**json_response)
        elif 'Organization' in object['className']:
            return Organization(**json_response)
        else:
            return ProviderGroup(**json_response)

    def create_provider(self, object: Businessman|NaturalPerson|Organization|ProviderGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Businessman|NaturalPerson|Organization|ProviderGroup:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'Businessman' in object['className']:
            return Businessman(**json_response)
        elif 'NaturalPerson' in object['className']:
            return NaturalPerson(**json_response)
        elif 'Organization' in object['className']:
            return Organization(**json_response)
        else:
            return ProviderGroup(**json_response)

    def update_provider(self, object: Businessman|NaturalPerson|Organization|ProviderGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Businessman|NaturalPerson|Organization|ProviderGroup:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'Businessman' in object['className']:
            return Businessman(**json_response)
        elif 'NaturalPerson' in object['className']:
            return NaturalPerson(**json_response)
        elif 'Organization' in object['className']:
            return Organization(**json_response)
        else:
            return ProviderGroup(**json_response)

    def remove_provider(self, object: Businessman|NaturalPerson|Organization|ProviderGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Businessman|NaturalPerson|Organization|ProviderGroup:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'Businessman' in object['className']:
            return Businessman(**json_response)
        elif 'NaturalPerson' in object['className']:
            return NaturalPerson(**json_response)
        elif 'Organization' in object['className']:
            return Organization(**json_response)
        else:
            return ProviderGroup(**json_response)

    def recover_provider(self, object: Businessman|NaturalPerson|Organization|ProviderGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Businessman|NaturalPerson|Organization|ProviderGroup:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'Businessman' in object['className']:
            return Businessman(**json_response)
        elif 'NaturalPerson' in object['className']:
            return NaturalPerson(**json_response)
        elif 'Organization' in object['className']:
            return Organization(**json_response)
        else:
            return ProviderGroup(**json_response)