from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.front.raspberry_terminal import RaspberryTerminal

class RaspberryTerminalOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "front.terminals.raspberry"

    def get_list_of_raspberry_terminal(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(RaspberryTerminal(**object))

        return result

    def get_tree_of_raspberry_terminal(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(RaspberryTerminal(**object))

        return result

    def get_raspberry_terminal(self, objectId: int, objectRid: int = None) -> RaspberryTerminal:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        return RaspberryTerminal(**json_response)

    def get_raspberry_terminal_with_subobjects(self, objectId: int, objectRid: int = None) -> RaspberryTerminal:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        return RaspberryTerminal(**json_response)

    def create_raspberry_terminal(self, object: RaspberryTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> RaspberryTerminal:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return RaspberryTerminal(**json_response)

    def update_raspberry_terminal(self, object: RaspberryTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> RaspberryTerminal:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return RaspberryTerminal(**json_response)

    def remove_raspberry_terminal(self, object: RaspberryTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> RaspberryTerminal:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return RaspberryTerminal(**json_response)

    def recover_raspberry_terminal(self, object: RaspberryTerminal,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> RaspberryTerminal:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return RaspberryTerminal(**json_response)