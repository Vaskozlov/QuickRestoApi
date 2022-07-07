from datetime import date
import json
import pandas

from operations_with_objects import OperationsWithObjects
from quick_resto_api import QuickRestoApi
from quick_resto_objects.modules.crm.accounting.account.account_type import AccountType
from quick_resto_objects.modules.crm.accounting.balance.account_balance import AccountBalance
from quick_resto_objects.modules.crm.customer.customer import CrmCustomer
from quick_resto_objects.modules.crm.customer.customer_token import CustomerToken
from quick_resto_objects.modules.front.cancellations.cancellation import Cancellation
from quick_resto_objects.modules.front.encashment.encashment import Encashment
from quick_resto_objects.modules.front.orders.order_info import OrderInfo
from quick_resto_objects.modules.front.preorders.preorder_info import PreorderInfo
from quick_resto_objects.modules.front.zreport.shift import Shift
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish import Dish
from quick_resto_objects.modules.warehouse.nomenclature.dish.dish_category import DishCategory
from quick_resto_objects.modules.warehouse.nomenclature.mods.modifier import Modifier
from quick_resto_objects.modules.warehouse.nomenclature.mods.modifier_group import ModifierGroup
from quick_resto_objects.modules.warehouse.nomenclature.semiproduct.semi_product import SemiProduct
from quick_resto_objects.modules.warehouse.nomenclature.semiproduct.store_category import StoreCategory
from quick_resto_objects.modules.warehouse.nomenclature.singleproduct.single_category import SingleCategory
from quick_resto_objects.modules.warehouse.nomenclature.singleproduct.single_product import SingleProduct


class QuickRestoInterface:
    def __init__(self, login: str, password: str, use_https: bool = True, layer: str = "quickresto.ru"):
        self._api: QuickRestoApi = QuickRestoApi(login, password, use_https, layer)
        self._operations_with_objects = OperationsWithObjects(self._api)
        self._ping()

    def convert_to_csv(self, json_data) -> str:
        if isinstance(json_data, dict):
            return pandas.DataFrame(json.loads(json.dumps(self._get_not_nested_json(json_data)))).to_csv()

        if isinstance(json_data, list):
            list_of_json_objects = list()

            for item in json_data:
                if isinstance(item, dict):
                    list_of_json_objects.append(self._get_not_nested_json(item))

            return pandas.DataFrame(json.loads(json.dumps(list_of_json_objects))).to_csv()

    def _get_not_nested_json(self, json:dict, result_json:dict = dict(), nested_names:list = list()) -> dict:
        for i in json.keys():
            if isinstance(json[i], dict):
                nested_names.append(i + "__")

                self._get_not_nested_json(json[i], result_json, nested_names)

                nested_names.pop()
            else:
                result_json["".join(nested_names) + i] =  json[i]

        return result_json

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

    # -------------
    def get_list_of_dishes(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("warehouse.nomenclature.dish",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        dishes = list()

        for dish in json_response:
            if 'DishCategory' in dish['className']:
                dishes.append(DishCategory(**dish))
            elif 'Dish' in dish['className']:
                dishes.append(Dish(**dish))

        return dishes

    def get_tree_of_dishes(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("warehouse.nomenclature.dish",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        dishes = list()

        for dish in json_response:
            if 'DishCategory' in dish['className']:
                dishes.append(DishCategory(**dish))
            elif 'Dish' in dish['className']:
                dishes.append(Dish(**dish))

        return dishes

    def get_dish_or_dish_category(self, objectId: int, objectRid: int = None) -> Dish | DishCategory:
        json_response = self._operations_with_objects.getObject("warehouse.nomenclature.dish", objectId, objectRid).json()

        if 'DishCategory' in json_response['className']:
            return DishCategory(**json_response)
        else:
            return Dish(**json_response)

    def get_dish_or_dish_category_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("warehouse.nomenclature.dish", objectId, objectRid).json()

        if 'DishCategory' in json_response['className']:
            return DishCategory(**json_response)
        else:
            return Dish(**json_response)

    def create_dish_or_dish_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Dish | DishCategory:

        json_response = self._operations_with_objects.createObject(object, "warehouse.nomenclature.dish", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'DishCategory' in json_response['className']:
            return DishCategory(**json_response)
        else:
            return Dish(**json_response)

    def update_dish_or_dish_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Dish | DishCategory:

        json_response = self._operations_with_objects.updateObject(object, "warehouse.nomenclature.dish", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'DishCategory' in json_response['className']:
            return DishCategory(**json_response)
        else:
            return Dish(**json_response)

    def remove_dish_or_dish_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Dish | DishCategory:

        json_response = self._operations_with_objects.removeObject(object, "warehouse.nomenclature.dish", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'DishCategory' in json_response['className']:
            return DishCategory(**json_response)
        else:
            return Dish(**json_response)

    def recover_dish_or_dish_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Dish | DishCategory:

        json_response = self._operations_with_objects.recoverObject(object, "warehouse.nomenclature.dish", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'DishCategory' in json_response['className']:
            return DishCategory(**json_response)
        else:
            return Dish(**json_response)

    # -------------
    def get_list_of_modifiers(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("warehouse.nomenclature.mods",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'ModifierGroup' in object['className']:
                result.append(ModifierGroup(**object))
            elif 'Modifier' in object['className']:
                result.append(Modifier(**object))

        return result

    def get_tree_of_modifiers(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("warehouse.nomenclature.mods",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'ModifierGroup' in object['className']:
                result.append(ModifierGroup(**object))
            elif 'Modifier' in object['className']:
                result.append(Modifier(**object))

        return result

    def get_modifiers_or_modifier_groups(self, objectId: int, objectRid: int = None) -> Modifier | ModifierGroup:
        json_response = self._operations_with_objects.getObject("warehouse.nomenclature.mods", objectId, objectRid).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def get_modifiers_or_modifier_groups_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("warehouse.nomenclature.mods", objectId, objectRid).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def create_modifiers_or_modifier_groups(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.createObject(object, "warehouse.nomenclature.mods", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def update_modifiers_or_modifier_groups(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.updateObject(object, "warehouse.nomenclature.mods", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def remove_modifiers_or_modifier_groups(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.removeObject(object, "warehouse.nomenclature.mods", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    def recover_modifiers_or_modifier_groups(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Modifier | ModifierGroup:

        json_response = self._operations_with_objects.recoverObject(object, "warehouse.nomenclature.mods", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'ModifierGroup' in json_response['className']:
            return ModifierGroup(**json_response)
        else:
            return Modifier(**json_response)

    # -------------
    def get_list_of_semi_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("warehouse.nomenclature.semiproduct",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'StoreCategory' in object['className']:
                result.append(StoreCategory(**object))
            elif 'SemiProduct' in object['className']:
                result.append(SemiProduct(**object))

        return result

    def get_tree_of_semi_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("warehouse.nomenclature.semiproduct",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'StoreCategory' in object['className']:
                result.append(StoreCategory(**object))
            elif 'SemiProduct' in object['className']:
                result.append(SemiProduct(**object))

        return result

    def get_semi_product_or_store_category(self, objectId: int, objectRid: int = None) -> SemiProduct | StoreCategory:
        json_response = self._operations_with_objects.getObject("warehouse.nomenclature.semiproduct", objectId, objectRid).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def get_semi_product_or_store_category_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("warehouse.nomenclature.semiproduct", objectId, objectRid).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def create_semi_product_or_store_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.createObject(object, "warehouse.nomenclature.semiproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def update_semi_product_or_store_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.updateObject(object, "warehouse.nomenclature.semiproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def remove_semi_product_or_store_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.removeObject(object, "warehouse.nomenclature.semiproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    def recover_semi_product_or_store_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SemiProduct | StoreCategory:

        json_response = self._operations_with_objects.recoverObject(object, "warehouse.nomenclature.semiproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'StoreCategory' in json_response['className']:
            return StoreCategory(**json_response)
        else:
            return SemiProduct(**json_response)

    # -------------
    def get_list_of_single_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("warehouse.nomenclature.singleproduct",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'SingleCategory' in object['className']:
                result.append(SingleCategory(**object))
            elif 'SingleProduct' in object['className']:
                result.append(SingleProduct(**object))

        return result

    def get_tree_of_single_product(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("warehouse.nomenclature.singleproduct",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            if 'SingleCategory' in object['className']:
                result.append(SingleCategory(**object))
            elif 'SingleProduct' in object['className']:
                result.append(SingleProduct(**object))

        return result

    def get_single_product_or_single_category(self, objectId: int, objectRid: int = None) -> SingleProduct | SingleCategory:
        json_response = self._operations_with_objects.getObject("warehouse.nomenclature.singleproduct", objectId, objectRid).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def get_single_product_or_single_category_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("warehouse.nomenclature.singleproduct", objectId, objectRid).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def create_single_product_or_single_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.createObject(object, "warehouse.nomenclature.singleproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def update_single_product_or_single_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.updateObject(object, "warehouse.nomenclature.singleproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def remove_single_product_or_single_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.removeObject(object, "warehouse.nomenclature.singleproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    def recover_single_product_or_single_category(self, object: Dish | DishCategory,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> SingleProduct | SingleCategory:

        json_response = self._operations_with_objects.recoverObject(object, "warehouse.nomenclature.singleproduct", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        if 'SingleCategory' in json_response['className']:
            return SingleCategory(**json_response)
        else:
            return SingleProduct(**json_response)

    # -------------
    def get_list_of_preorder_info(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("front.preorders",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(PreorderInfo(**object))

        return result

    def get_tree_of_preorder_info(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("front.preorders",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(PreorderInfo(**object))

        return result

    def get_preorder_info(self, objectId: int, objectRid: int = None) -> PreorderInfo:
        json_response = self._operations_with_objects.getObject("front.preorders", objectId, objectRid).json()

        return PreorderInfo(**json_response)

    def get_preorder_info_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("front.preorders", objectId, objectRid).json()

        return PreorderInfo(**json_response)

    def create_preorder_info(self, object: PreorderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PreorderInfo:

        json_response = self._operations_with_objects.createObject(object, "front.preorders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return PreorderInfo(**json_response)

    def update_preorder_info(self, object: PreorderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PreorderInfo:

        json_response = self._operations_with_objects.updateObject(object, "front.preorders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return PreorderInfo(**json_response)

    def remove_preorder_info(self, object: PreorderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PreorderInfo:

        json_response = self._operations_with_objects.removeObject(object, "front.preorders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return PreorderInfo(**json_response)

    def recover_preorder_info(self, object: PreorderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> PreorderInfo:

        json_response = self._operations_with_objects.recoverObject(object, "front.preorders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return PreorderInfo(**json_response)

    # -------------
    def get_list_of_order_info(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("front.orders",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(OrderInfo(**object))

        return result

    def get_tree_of_order_info(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("front.orders",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(OrderInfo(**object))

        return result

    def get_order_info(self, objectId: int, objectRid: int = None) -> OrderInfo:
        json_response = self._operations_with_objects.getObject("front.orders", objectId, objectRid).json()

        return OrderInfo(**json_response)

    def get_order_info_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("front.orders", objectId, objectRid).json()

        return OrderInfo(**json_response)

    def create_order_info(self, object: OrderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OrderInfo:

        json_response = self._operations_with_objects.createObject(object, "front.orders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OrderInfo(**json_response)

    def update_order_info(self, object: OrderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OrderInfo:

        json_response = self._operations_with_objects.updateObject(object, "front.orders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OrderInfo(**json_response)

    def remove_order_info(self, object: OrderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OrderInfo:

        json_response = self._operations_with_objects.removeObject(object, "front.orders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OrderInfo(**json_response)

    def recover_order_info(self, object: OrderInfo,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> OrderInfo:

        json_response = self._operations_with_objects.recoverObject(object, "front.orders", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return OrderInfo(**json_response)

    # -------------
    def get_list_of_cancellations(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("front.cancellations",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(Cancellation(**object))

        return result

    def get_tree_of_cancellations(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("front.cancellations",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(Cancellation(**object))

        return result

    def get_cancellations(self, objectId: int, objectRid: int = None) -> Cancellation:
        json_response = self._operations_with_objects.getObject("front.cancellations", objectId, objectRid).json()

        return Cancellation(**json_response)

    def get_cancellations_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("front.cancellations", objectId, objectRid).json()

        return Cancellation(**json_response)

    def create_cancellation(self, object: Cancellation,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Cancellation:

        json_response = self._operations_with_objects.createObject(object, "front.cancellations", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Cancellation(**json_response)

    def update_cancellation(self, object: Cancellation,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Cancellation:

        json_response = self._operations_with_objects.updateObject(object, "front.cancellations", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Cancellation(**json_response)

    def remove_cancellation(self, object: Cancellation,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Cancellation:

        json_response = self._operations_with_objects.removeObject(object, "front.cancellations", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Cancellation(**json_response)

    def recover_cancellation(self, object: Cancellation,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Cancellation:

        json_response = self._operations_with_objects.recoverObject(object, "front.cancellations", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Cancellation(**json_response)

    # -------------
    def get_list_of_encashment(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("front.encashment",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(Encashment(**object))

        return result

    def get_tree_of_encashment(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("front.encashment",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(Encashment(**object))

        return result

    def get_encashment(self, objectId: int, objectRid: int = None) -> Encashment:
        json_response = self._operations_with_objects.getObject("front.encashment", objectId, objectRid).json()

        return Encashment(**json_response)

    def get_encashment_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("front.encashment", objectId, objectRid).json()

        return Encashment(**json_response)

    def create_encashment(self, object: Encashment,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Encashment:

        json_response = self._operations_with_objects.createObject(object, "front.encashment", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Cancellation(**json_response)

    def update_encashment(self, object: Encashment,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Encashment:

        json_response = self._operations_with_objects.updateObject(object, "front.encashment", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Encashment(**json_response)

    def remove_encashment(self, object: Encashment,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Encashment:

        json_response = self._operations_with_objects.removeObject(object, "front.encashment", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Encashment(**json_response)

    def recover_encashment(self, object: Encashment,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Encashment:

        json_response = self._operations_with_objects.recoverObject(object, "front.encashment", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Encashment(**json_response)

    # -------------
    def get_list_of_shift(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getList("front.zreport",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(Shift(**object))

        return result

    def get_tree_of_shift(self, ownerContextId: int = None, ownerContextClassName: str = None,
                           showDeleted: bool = False) -> list:

        json_response = self._operations_with_objects.getTree("front.zreport",
                                                              ownerContextId, ownerContextClassName, showDeleted).json()

        result = list()

        for object in json_response:
            result.append(Shift(**object))

        return result

    def get_shift(self, objectId: int, objectRid: int = None) -> Shift:
        json_response = self._operations_with_objects.getObject("front.zreport", objectId, objectRid).json()

        return Shift(**json_response)

    def get_shift_with_subobjects(self, objectId: int, objectRid: int = None) -> list:
        json_response = self._operations_with_objects.getObjectWithSubobjects("front.zreport", objectId, objectRid).json()

        return Shift(**json_response)

    def create_shift(self, object: Shift,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Shift:

        json_response = self._operations_with_objects.createObject(object, "front.zreport", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Cancellation(**json_response)

    def update_shift(self, object: Shift,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Shift:

        json_response = self._operations_with_objects.updateObject(object, "front.zreport", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Shift(**json_response)

    def remove_shift(self, object: Shift,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Shift:

        json_response = self._operations_with_objects.removeObject(object, "front.zreport", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Shift(**json_response)

    def recover_shift(self, object: Shift,ownerContextId: int = None,
                                                ownerContextClassName: str = None, parentContextId: int = None,
                                                parentContextClassName: str = None) -> Shift:

        json_response = self._operations_with_objects.recoverObject(object, "front.zreport", ownerContextId, 
                                                ownerContextClassName, parentContextId, parentContextClassName).json()

        return Shift(**json_response)
