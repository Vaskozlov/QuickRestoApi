from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_objects.modules.warehouse.modifier import Modifier
from quick_resto_objects.modules.warehouse.modifier_group import ModifierGroup
from quick_resto_api.quick_resto_api import QuickRestoApi

class ModifierOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "warehouse.nomenclature.mods"

    def get_list_of_modifiers(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'ModifierGroup' in object['className']:
                result.append(ModifierGroup(**object))
            elif 'Modifier' in object['className']:
                result.append(Modifier(**object))

        return result

    def get_tree_of_modifiers(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'ModifierGroup' in object['className']:
                result.append(ModifierGroup(**object))
            elif 'Modifier' in object['className']:
                result.append(Modifier(**object))

        return result

    def get_modifiers_or_modifier_groups(self, objectId: int, objectRid: int = None) -> Modifier | ModifierGroup:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def get_modifiers_or_modifier_groups_with_subobjects(self, objectId: int, objectRid: int = None) -> Modifier | ModifierGroup:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def create_modifiers_or_modifier_groups(self, object: Modifier | ModifierGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def update_modifiers_or_modifier_groups(self, object: Modifier | ModifierGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def remove_modifiers_or_modifier_groups(self, object: Modifier | ModifierGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def recover_modifiers_or_modifier_groups(self, object: Modifier | ModifierGroup,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    