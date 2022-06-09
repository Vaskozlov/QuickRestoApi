import sys
from pprint import pprint
from quick_resto_interface import QuickRestoInterface

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
data = interface.get_dishes()

pprint(data)
