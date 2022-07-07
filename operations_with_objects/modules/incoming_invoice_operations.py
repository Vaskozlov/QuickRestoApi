from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.warehouse.documents.incoming.incoming_invoice import IncomingInvoice

class IncomingInvoiceOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "warehouse.documents.incoming"

    def get_list_of_incoming_invoice(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(IncomingInvoice(**object))

        return result

    def get_tree_of_incoming_invoice(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(IncomingInvoice(**object))

        return result

    def get_incoming_invoice(self, objectId: int, objectRid: int = None) -> IncomingInvoice:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        return IncomingInvoice(**json_response)

    def get_incoming_invoice_with_subobjects(self, objectId: int, objectRid: int = None) -> IncomingInvoice:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        return IncomingInvoice(**json_response)

    def create_incoming_invoice(self, object: IncomingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> IncomingInvoice:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return IncomingInvoice(**json_response)

    def update_incoming_invoice(self, object: IncomingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> IncomingInvoice:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return IncomingInvoice(**json_response)

    def remove_incoming_invoice(self, object: IncomingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> IncomingInvoice:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return IncomingInvoice(**json_response)

    def recover_incoming_invoice(self, object: IncomingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> IncomingInvoice:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return IncomingInvoice(**json_response)