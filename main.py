import sys
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2], True, "quickresto.ru")

dishes = interface.get_list_of_dishes()

for dish in dishes:
    print(dish)
