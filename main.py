import sys
import pprint
from quick_resto_interface import QuickRestoInterface
from quick_resto_objects.dish.dish_category import DishCategory
from quick_resto_objects.dish.dish import Dish

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
data = list(interface.get_dishes())

# pprint.pprint(data[0])
DishCategory(**data[0])

dish = Dish(**data[1])
pprint.pprint(data[1]['dishSales'][0]['cookingPlace']['store'])
