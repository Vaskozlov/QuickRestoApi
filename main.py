import sys
import pprint
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2])
pprint.pprint(interface.get_dishes())
