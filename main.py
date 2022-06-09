import sys
from pprint import pprint
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
interface.get_dishes()
interface.get_stores()

data = interface.get_customer_info("67666600000014=2012")
pprint(data)
pprint(CrmCustomer(**data))
