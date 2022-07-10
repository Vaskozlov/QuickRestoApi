from quick_resto_objects.modules.personnel.employee import Employee
from quick_resto_objects.quick_resto_object import QuickRestoObject


class Cancellation(QuickRestoObject):
    @property
    def comment(self) -> str:
        return self._comment

    @property
    def description(self) -> str:
        return self._description

    @property
    def parent_order_doc_id(self) -> str:
        return self._parent_order_doc_id

    @property
    def with_dismission(self) -> bool:
        return self._with_dismission

    @property
    def employee(self) -> Employee:
        return self._employee

    @property
    def parent_return_order_doc_id(self) -> str:
        return self._parent_return_order_doc_id

    @property
    def table_order_doc_id(self) -> str:
        return self._table_order_doc_id

    def __init__(self, comment: str = None, description: str = None, parentOrderDocId: str = None,
                 withDismission: bool = None,
                 employee: dict = None, parentReturnOrderDocId: str = None, tableOrderDocId: str = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.front.cancellations.Cancellation"

        super().__init__(class_name=class_name, **kwargs)

        self._comment: str = comment
        self._description: str = description
        self._parent_order_doc_id: str = parentOrderDocId
        self._with_dismission: bool = withDismission

        if employee is not None: 
            self._employee = Employee(**employee)
        else:
            self._employee = None

        self._parent_return_order_doc_id: str = parentReturnOrderDocId
        self._table_order_doc_id: str = tableOrderDocId
