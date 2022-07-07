from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.front.terminals.kkm.kkm_terminal import KkmTerminal
from quick_resto_objects.modules.front.terminals.kkm.virtual_kkm_terminal import VirtualKkmTerminal

class KkmTerminalOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "front.terminals.kkm"

    def get_list_of_terminal(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'KkmTerminal' in object['className']:
                result.append(KkmTerminal(**object))
            elif 'VirtualKkmTerminal' in object['className']:
                result.append(VirtualKkmTerminal(**object))

        return result

    def get_tree_of_terminal(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'KkmTerminal' in object['className']:
                result.append(KkmTerminal(**object))
            elif 'VirtualKkmTerminal' in object['className']:
                result.append(VirtualKkmTerminal(**object))

        return result

    def get_terminal(self, objectId: int, objectRid: int = None) -> KkmTerminal|VirtualKkmTerminal:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        if 'KkmTerminal' in json_response['className']:
            return KkmTerminal(**json_response)
        else:
            return VirtualKkmTerminal(**json_response)

    def get_terminal_with_subobjects(self, objectId: int, objectRid: int = None) -> KkmTerminal|VirtualKkmTerminal:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        if 'KkmTerminal' in json_response['className']:
            return KkmTerminal(**json_response)
        else:
            return VirtualKkmTerminal(**json_response)

    def create_terminal(self, object: KkmTerminal|VirtualKkmTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> KkmTerminal|VirtualKkmTerminal:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'KkmTerminal' in json_response['className']:
            return KkmTerminal(**json_response)
        else:
            return VirtualKkmTerminal(**json_response)

    def update_terminal(self, object: KkmTerminal|VirtualKkmTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> KkmTerminal|VirtualKkmTerminal:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'KkmTerminal' in json_response['className']:
            return KkmTerminal(**json_response)
        else:
            return VirtualKkmTerminal(**json_response)

    def remove_terminal(self, object: KkmTerminal|VirtualKkmTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> KkmTerminal|VirtualKkmTerminal:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'KkmTerminal' in json_response['className']:
            return KkmTerminal(**json_response)
        else:
            return VirtualKkmTerminal(**json_response)

    def recover_terminal(self, object: KkmTerminal|VirtualKkmTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> KkmTerminal|VirtualKkmTerminal:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'KkmTerminal' in json_response['className']:
            return KkmTerminal(**json_response)
        else:
            return VirtualKkmTerminal(**json_response)