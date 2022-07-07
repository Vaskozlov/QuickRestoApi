from operations_with_objects.operations_with_objects import OperationsWithObjects
from operations_with_objects.system_object import SystemObject
from quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.warehouse.documents.outgoing.outgoing_invoice import OutgoingInvoice

class OutgoingInvoiceOperations(SystemObject):
    def __init__(self, api: QuickRestoApi):
        self._operations_with_objects = OperationsWithObjects(api)

        self._module_name:str = "warehouse.documents.outgoing"

    def get_list_of_outgoing_invoice(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(OutgoingInvoice(**object))

        return result

    def get_tree_of_outgoing_invoice(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree(self._module_name,
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(OutgoingInvoice(**object))

        return result

    def get_outgoing_invoice(self, objectId: int, objectRid: int = None) -> OutgoingInvoice:
        json_response = self._operations_with_objects.getObject(self._module_name, objectId, objectRid).json()

        return OutgoingInvoice(**json_response)

    def get_outgoing_invoice_with_subobjects(self, objectId: int, objectRid: int = None) -> OutgoingInvoice:
        json_response = self._operations_with_objects.getObjectWithSubobjects(self._module_name, objectId, objectRid).json()

        return OutgoingInvoice(**json_response)

    def create_outgoing_invoice(self, object: OutgoingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OutgoingInvoice:

        json_response = self._operations_with_objects.createObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OutgoingInvoice(**json_response)

    def update_outgoing_invoice(self, object: OutgoingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OutgoingInvoice:

        json_response = self._operations_with_objects.updateObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OutgoingInvoice(**json_response)

    def remove_outgoing_invoice(self, object: OutgoingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OutgoingInvoice:

        json_response = self._operations_with_objects.removeObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OutgoingInvoice(**json_response)

    def recover_outgoing_invoice(self, object: OutgoingInvoice,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OutgoingInvoice:

        json_response = self._operations_with_objects.recoverObject(object, self._module_name, ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OutgoingInvoice(**json_response)