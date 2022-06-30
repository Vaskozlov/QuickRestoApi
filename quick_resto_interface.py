from datetime import date, datetime
import requests
from operations_with_objects import OperationsWithObjects
from quick_resto_api import QuickRestoApi
from quick_resto_objects.store.store import Store
from quick_resto_objects.nomenclature.dish.dish import Dish
from quick_resto_objects.crm.customer.token_types import TokenType, EntryType
from quick_resto_objects.crm.customer.customer import CrmCustomer
from quick_resto_objects.nomenclature.dish.dish_category import DishCategory
from quick_resto_objects.nomenclature.singleproduct import SingleProduct


class QuickRestoInterface:
    def __init__(self, login: str, password: str, use_https: bool = True, layer: str = "quickresto.ru"):
        self._api: QuickRestoApi = QuickRestoApi(login, password, use_https, layer)
        self._operations_with_objects = OperationsWithObjects(QuickRestoApi)
        self._ping()

    def _ping(self) -> None:
        # TODO: add good error message for this case
        self._api.get("ping")

    def crm_search_client(self, search: str) -> dict:
        json_data = {
            "search": search
        }

        return self._api.post("bonuses/filterCustomers", json_data=json_data).json()

    def crm_get_customer_info(self, key: str, token_type: TokenType = TokenType.CARD,
                          entry_type: EntryType = EntryType.TRACK_CODE) -> CrmCustomer:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            }
        }

        json_response = self._api.post("bonuses/customerInfo", json_data=json_data).json()

        return CrmCustomer(**json_response)

    def crm_get_client_balance(self, key: str, bonus_account_type: int, token_type: TokenType = TokenType.CARD,
                           entry_type: EntryType = EntryType.TRACK_CODE) -> dict:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            },
            "accountType": {
                "accountGuid": f"bonus_account_type-{bonus_account_type}"
            }
        }

        return self._api.post("bonuses/balance", json_data=json_data).json()

    def crm_get_operation_history(self, key: str, bonus_account_type: int, token_type: TokenType = TokenType.CARD,
                           entry_type: EntryType = EntryType.TRACK_CODE) -> dict:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            },
            "accountType": {
                "accountGuid": f"bonus_account_type-{bonus_account_type}"
            }
        }

        return self._api.post("bonuses/operationHistory", json_data = json_data).json()

    def crm_create_customer(self, customer: CrmCustomer) -> CrmCustomer:
        json_response = self._api.post("bonuses/createCustomer", json_data = customer.__str__.__dict__).json()

        return CrmCustomer(**json_response)

    def crm_depit_hold(self, key: str, bonus_account_type: int, amount: int, token_type: TokenType = TokenType.CARD,
                           entry_type: EntryType = EntryType.TRACK_CODE, date: date = None, precheckID: int = None) -> dict:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            },
            "date": date,
            "precheck": precheckID,
            "accountType": {
                "accountGuid": f"bonus_account_type-{bonus_account_type}"
            },
            "amount": amount
        }

        return self._api.post("bonuses/debitHold", json_data = json_data).json()

    def crm_credit_hold(self, key: str, bonus_account_type: int, amount: int, token_type: TokenType = TokenType.CARD,
                           entry_type: EntryType = EntryType.TRACK_CODE, date: date = None, precheckID: int = None) -> dict:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            },
            "date": date,
            "precheck": precheckID,
            "accountType": {
                "accountGuid": f"bonus_account_type-{bonus_account_type}"
            },
            "amount": amount
        }

        return self._api.post("bonuses/creditHold", json_data = json_data).json()

    def crm_reverse(self, key: str, bonus_account_type: int, amount: int, bonusTransactionId: int, token_type: TokenType = TokenType.CARD,
                           entry_type: EntryType = EntryType.TRACK_CODE, date: date = None, precheckID: int = None) -> dict:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            },
            "date": date,
            "precheck": precheckID,
            "accountType": {
                "accountGuid": f"bonus_account_type-{bonus_account_type}"
            },
            "amount": amount,
            "bonusTransactionId": bonusTransactionId
        }

        return self._api.post("bonuses/reverse", json_data = json_data).json()
    
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
        return self._get_system_object("personnel.employee").json()

    def _get_system_object(self, url: str) -> requests.Response:
        return self._api.get(f"api/list?moduleName={url}")
