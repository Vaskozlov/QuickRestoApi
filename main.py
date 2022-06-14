import sys
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
dishes = interface.get_dishes()
stores = interface.get_stores()

# print(stores)
# print(dishes)

customer = interface.get_customer_info("66666600000014=2012")
