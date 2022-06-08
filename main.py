import sys
from pprint import pprint
from quick_resto_interface import QuickRestoInterface
from quick_resto_objects.nomenclature.dish.dish_category import DishCategory
from quick_resto_objects.nomenclature.dish.dish import Dish

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
data = list(interface.get_dishes())

# pprint.pprint(data[0])
DishCategory(**data[0])

dish = Dish(**data[1])
pprint(data[1]['dishSales'][0]['salePlace'])
