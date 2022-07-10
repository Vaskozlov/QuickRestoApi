from quick_resto_objects.modules.warehouse.sale_place import SalePlace
from quick_resto_objects.platform.role import Role
from quick_resto_objects.quick_resto_object import QuickRestoObject


class PaymentType(QuickRestoObject):
    @property
    def name(self) -> str:
        return self._name

    @property
    def type(self) -> str:
        return self._type

    @property
    def operation_type(self) -> str:
        return self._operation_type

    @property
    def partial_allowed(self) -> bool:
        return self._partial_allowed

    @property
    def seq(self) -> int:
        return self._seq

    @property
    def require_admin_confirmation(self) -> bool:
        return self._require_admin_confirmation

    @property
    def require_customer_confirmation(self) -> bool:
        return self._require_customer_confirmation

    @property
    def customer_type(self) -> str:
        return self._customer_type

    @property
    def payment_mechanism_web(self) -> str:
        return self._payment_mechanism_web

    @property
    def allowed_organizations_web(self) -> list:
        return self._allowed_organizations_web

    @property
    def allowed_sale_places_web(self) -> list:
        return self._allowed_sale_places_web

    @property
    def employee_roles_web(self) -> list:
        return self._employee_roles_web

    @property
    def concrete_employees_web(self) -> list:
        return self._concrete_employees_web

    @property
    def allowed_user_roles_web(self) -> list:
        return self._allowed_user_roles_web

    @property
    def allowed_concrete_users_web(self) -> list:
        return self._allowed_concrete_users_web

    @property
    def guest_groups_web(self) -> list:
        return self._guest_groups_web

    @property
    def concrete_guests_web(self) -> list:
        return self._concrete_guests_web

    @property
    def partner_groups_web(self) -> list:
        return self._partner_groups_web

    @property
    def concrete_partners_web(self) -> list:
        return self._concrete_partners_web

    def __init__(self, name: str = None, type: str = None, operationType: str = None, partialAllowed: bool = None,
                 seq: int = None, requireAdminConfirmation: bool = None,
                 requireCustomerConfirmation: bool = None, customerType: str = None, paymentMechanismWeb: str = None,
                 allowedOrganizationsWeb: list = None,
                 allowedSalePlacesWeb: list = None, employeeRolesWeb: list = None, concreteEmployeesWeb: list = None,
                 allowedUserRolesWeb: list = None,
                 allowedConcreteUsersWeb: list = None, guestGroupsWeb: list = None, concreteGuestsWeb: list = None,
                 partnerGroupsWeb: list = None,
                 concretePartnersWeb: list = None, **kwargs):
        class_name = "ru.edgex.quickresto.modules.core.dictionaries.paymenttypes.PaymentType"

        super().__init__(class_name=class_name, **kwargs)

        self._name: str = name
        self._type: str = type
        self._operation_type: str = operationType
        self._partial_allowed: bool = partialAllowed
        self._seq: int = seq
        self._require_admin_confirmation: bool = requireAdminConfirmation
        self._require_customer_confirmation: bool = requireCustomerConfirmation
        self._customer_type: str = customerType
        self._payment_mechanism_web: str = paymentMechanismWeb
        self._allowed_organizations_web: list = allowedOrganizationsWeb

        if allowedSalePlacesWeb is not None: 
            self._allowed_sale_places_web: list = [SalePlace(**place) for place in allowedSalePlacesWeb]
        else:
            self._allowed_sale_places_web = None
        
        self._employee_roles_web: list = employeeRolesWeb
        self._concrete_employees_web: list = concreteEmployeesWeb

        if allowedUserRolesWeb is not None: 
            self._allowed_user_roles_web: list = [Role(**value) for value in allowedUserRolesWeb]
        else:
            self._allowed_user_roles_web = None

        self._allowed_concrete_users_web: list = allowedConcreteUsersWeb
        self._guest_groups_web: list = guestGroupsWeb
        self._concrete_guests_web: list = concreteGuestsWeb
        self._partner_groups_web: list = partnerGroupsWeb
        self._concrete_partners_web: list = concretePartnersWeb
