import sys
from pprint import pprint
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2], False, "qa.ru")

employees = interface.get_employees()
pprint(employees)
