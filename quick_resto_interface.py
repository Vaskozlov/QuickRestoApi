import pprint

import requests
from enum import Enum
from quick_resto_api import QuickRestoApi
from quick_resto_objects.store.store import Store
from quick_resto_objects.crm.customer.customer import CrmCustomer
from quick_resto_objects.nomenclature.dish.dish import Dish
from quick_resto_objects.nomenclature.dish.dish_category import DishCategory


class TokenType(Enum):
    PIN = "pin"
    CARD = "card"
    PHONE = "phone"
    QR_GUEST = "qrGuest"


class EntryType(Enum):
    BAR_CODE = "barCode"
    TRACK_CODE = "trackCode"
    QR_CODE = "qrCode"
    MANUAL = "manual"


class QuickRestoInterface:
    def __init__(self, login, password):
        self._api: QuickRestoApi = QuickRestoApi(login, password)
        self._ping()

    def _ping(self) -> None:
        # TODO: add good error message for this case
        self._api.get("ping")

    def get_stores(self) -> set:
        stores = set()

        for store in self._get_system_object("warehouse.store").json():
            if 'Store' in store['className']:
                stores.add(Store(**store))

        return stores

    def get_dishes(self) -> set:
        dishes = set()
        json_data = self._get_system_object("warehouse.nomenclature.dish").json()

        for dish in json_data:
            if 'DishCategory' in dish['className']:
                dishes.add(DishCategory(**dish))
            elif 'Dish' in dish['className']:
                dishes.add(Dish(**dish))

        return dishes

    def get_table_orders(self) -> dict:
        return self._get_system_object("front.tableorders").json()

    def get_products(self) -> dict:
        return self._get_system_object("warehouse.nomenclature.singleproduct").json()

    def get_employees(self) -> dict:
        return self._get_system_object("personnel.employee").json()

    def _get_system_object(self, url: str) -> requests.Response:
        return self._api.get(f"api/list?moduleName={url}")

    def get_customer_info(self, key: str, token_type: TokenType = TokenType.CARD,
                          entry_type: EntryType = EntryType.TRACK_CODE) -> dict:
        json_data = {
            "customerToken": {
                "type": token_type.value,
                "entry": entry_type.value,
                "key": key
            }
        }

        return self._api.post("bonuses/customerInfo", json_data=json_data).json()

    def search_client(self, search: str) -> dict:
        json_data = {
            "search": search
        }

        return self._api.post("bonuses/filterCustomers", json_data=json_data).json()

    def get_client_balance(self, key: str, bonus_account_type: int, token_type: TokenType = TokenType.CARD,
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
