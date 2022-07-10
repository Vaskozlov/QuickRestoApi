from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api.quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.core.measure_unit import MeasureUnit

class MeasureUnitOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "core.dictionaries.measureunits"

    def get_list_of_measure_unit(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(MeasureUnit(**object))

        return result

    def get_tree_of_measure_unit(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(MeasureUnit(**object))

        return result

    def get_measure_unit(self, objectId: int, objectRid: int = None) -> MeasureUnit:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        return MeasureUnit(**json_response)

    def get_measure_unit_with_subobjects(self, objectId: int, objectRid: int = None) -> MeasureUnit:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        return MeasureUnit(**json_response)

    def create_measure_unit(self, object: MeasureUnit,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> MeasureUnit:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return MeasureUnit(**json_response)

    def update_measure_unit(self, object: MeasureUnit,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> MeasureUnit:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return MeasureUnit(**json_response)

    def remove_measure_unit(self, object: MeasureUnit,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> MeasureUnit:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return MeasureUnit(**json_response)

    def recover_measure_unit(self, object: MeasureUnit,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> MeasureUnit:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return MeasureUnit(**json_response)