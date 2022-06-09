import sys
from pprint import pprint
from quick_resto_interface import QuickRestoInterface

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
interface.get_dishes()
data = interface.get_stores()

pprint(data)
