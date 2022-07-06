from datetime import date

import requests

from operations_with_objects import OperationsWithObjects
from quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.crm.accounting.account.account_type import AccountType
from quick_resto_objects.modules.crm.accounting.balance.account_balance import AccountBalance
from quick_resto_objects.modules.crm.customer.customer import CrmCustomer
from quick_resto_objects.modules.crm.customer.customer_token import CustomerToken
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish import Dish
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish_category import DishCategory
from quick_resto_objects.modules.warehouse.nomenclature.singleproduct.single_product import SingleProduct
from quick_resto_objects.modules.warehouse.store.store import Store


class QuickRestoInterface:
    def __init__(self, login: str, password: str, use_https: bool = True, layer: str = "quickresto.ru"):
        self._api: QuickRestoApi = QuickRestoApi(login, password, use_https, layer)
        self._operations_with_objects = OperationsWithObjects(self._api)
        self._ping()

    def _ping(self) -> None:
        # TODO: add good error message for this case
        self._api.get("ping")

    def crm_search_client(self, search: str) -> CrmCustomer:
        json_data = {
            "search": search
        }

        json_response = self._api.post("bonuses/filterCustomers", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_get_customer_info(self, customerToken: CustomerToken) -> CrmCustomer:
        json_data = {
            "customerToken": customerToken.get_json_object
        }

        json_response = self._api.post("bonuses/customerInfo", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_get_client_balance(self, customerToken: CustomerToken, accountType: AccountType) -> AccountBalance:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "accountType": accountType.get_json_object()
        }

        json_response = self._api.post("bonuses/balance", json_data=json_data).json()

        return AccountBalance(**json_response)

    def crm_get_operation_history(self, customerToken: CustomerToken) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object()
        }

        json_response = self._api.post("bonuses/operationHistory", json_data=json_data).json()

        return json_response

    def crm_create_customer(self, customer: CrmCustomer) -> CrmCustomer:
        json_data = customer.get_json_object()

        json_response = self._api.post("bonuses/createCustomer", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_depit_hold(self, customerToken: CustomerToken, amount: int, accountType: AccountType, date: date = None,
                       precheck: int = None) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "date": date,
            "precheck": precheck,
            "amount": amount,
            "accountType": accountType.get_json_object(),
        }

        json_response = self._api.post("bonuses/debitHold", json_data=json_data).json()

        return json_response

    def crm_credit_hold(self, customerToken: CustomerToken, accountType: AccountType, amount: int, date: date = None,
                        precheck: int = None) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "date": date,
            "precheck": precheck,
            "amount": amount,
            "accountType": accountType.get_json_object(),
        }

        json_response = self._api.post("bonuses/creditHold", json_data=json_data).json()

        return json_response

    def crm_reverse(self, customerToken: CustomerToken, accountType: AccountType, amount: int, bonusTransactionId: int,
                    date: date = None, precheck: int = None) -> dict:
        json_data = {
            "customerToken": customerToken.get_json_object(),
            "date": date,
            "precheck": precheck,
            "amount": amount,
            "accountType": accountType.get_json_object(),
            "bonusTransactionId": bonusTransactionId
        }

        json_response = self._api.post("bonuses/reverse", json_data=json_data).json()

        return json_response

    def get_list_of_dishes(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> set:

        json_response = self._operations_with_objects.getList("warehouse.nomenclature.dish",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        dishes = set()

        for dish in json_response:
            if 'DishCategory' in dish['className']:
                dishes.add(DishCategory(**dish))
            elif 'Dish' in dish['className']:
                dishes.add(Dish(**dish))

        return dishes

    def get_stores(self) -> set:
        stores = set()

        for store in self._get_system_object("warehouse.store").json():
            if 'Store' in store['className']:
                stores.add(Store(**store))

        return stores

    def get_table_orders(self) -> dict:
        return self._get_system_object("front.tableorders").json()

    def get_products(self) -> set:
        products = set()
        json_response = self._get_system_object("warehouse.nomenclature.singleproduct").json()

        for product in json_response:
            products.add(SingleProduct(**product))

        return products

    def get_employees(self) -> dict:
        return self._operations_with_objects.getList("personnel.employee").json()

    def _get_system_object(self, url: str) -> requests.Response:
        return self._api.get(f"api/list?moduleName={url}")
