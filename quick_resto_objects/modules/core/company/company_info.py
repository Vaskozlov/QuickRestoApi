from quick_resto_objects.quick_resto_object import QuickRestoObject


class CompanyInfo(QuickRestoObject):
    @property
    def account(self) -> str:
        return self._account

    @property
    def address(self) -> str:
        return self._address

    @property
    def bank_id(self) -> str:
        return self._bank_id

    @property
    def bank_name(self) -> str:
        return self._bank_name

    @property
    def correspondent_account(self) -> str:
        return self._correspondent_account

    @property
    def delivery_address(self) -> str:
        return self._delivery_address

    @property
    def deleted(self) -> bool:
        return self._deleted

    @property
    def inn_code(self) -> str:
        return self._inn_code

    @property
    def kpp_code(self) -> str:
        return self._kpp_code

    @property
    def name(self) -> str:
        return self._name

    @property
    def okpo_code(self) -> str:
        return self._okpo_code

    @property
    def short_name(self) -> str:
        return self._short_name

    def __init__(self, account: str, address: str, bankId: str, bankName: str, correspondentAccount: str,
                 deliveryAddress: str, deleted: bool, innCode: str, kppCode: str, name: str, okpoCode: str,
                 shortName: str, **kwargs):
        class_name = "ru.edgex.quickresto.modules.core.company.CompanyInfo"

        super().__init__(class_name=class_name, **kwargs)

        self._account: str = account
        self._address: str = address
        self._bank_id: str = bankId
        self._bank_name: str = bankName
        self._correspondent_account: str = correspondentAccount
        self._delivery_address: str = deliveryAddress
        self._deleted: bool = deleted
        self._inn_code: str = innCode
        self._kpp_code: str = kppCode
        self._name: str = name
        self._okpo_code: str = okpoCode
        self._short_name: str = shortName
