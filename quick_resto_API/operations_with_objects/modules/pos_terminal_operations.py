from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.front.pos_terminal import PosTerminal
from quick_resto_objects.modules.front.virtual_pos_terminal import VirtualPosTerminal

class PosTerminalOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "front.terminals.pos"

    def get_list_of_terminal(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'PosTerminal' in object['className']:
                result.append(PosTerminal(**object))
            elif 'VirtualPosTerminal' in object['className']:
                result.append(VirtualPosTerminal(**object))

        return result

    def get_tree_of_terminal(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'PosTerminal' in object['className']:
                result.append(PosTerminal(**object))
            elif 'VirtualPosTerminal' in object['className']:
                result.append(VirtualPosTerminal(**object))

        return result

    def get_terminal(self, objectId: int, objectRid: int = None) -> PosTerminal|VirtualPosTerminal:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        if 'PosTerminal' in json_response['className']:
            return PosTerminal(**json_response)
        else:
            return VirtualPosTerminal(**json_response)

    def get_terminal_with_subobjects(self, objectId: int, objectRid: int = None) -> PosTerminal|VirtualPosTerminal:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        if 'PosTerminal' in json_response['className']:
            return PosTerminal(**json_response)
        else:
            return VirtualPosTerminal(**json_response)

    def create_terminal(self, object: PosTerminal|VirtualPosTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PosTerminal|VirtualPosTerminal:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'PosTerminal' in json_response['className']:
            return PosTerminal(**json_response)
        else:
            return VirtualPosTerminal(**json_response)

    def update_terminal(self, object: PosTerminal|VirtualPosTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PosTerminal|VirtualPosTerminal:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'PosTerminal' in json_response['className']:
            return PosTerminal(**json_response)
        else:
            return VirtualPosTerminal(**json_response)

    def remove_terminal(self, object: PosTerminal|VirtualPosTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PosTerminal|VirtualPosTerminal:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'PosTerminal' in json_response['className']:
            return PosTerminal(**json_response)
        else:
            return VirtualPosTerminal(**json_response)

    def recover_terminal(self, object: PosTerminal|VirtualPosTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PosTerminal|VirtualPosTerminal:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'PosTerminal' in json_response['className']:
            return PosTerminal(**json_response)
        else:
            return VirtualPosTerminal(**json_response)