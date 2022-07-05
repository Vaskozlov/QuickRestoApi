import sys

from class_generator import QuickRestoClassGenerator
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2], True, "quickresto.ru")

employees = interface.get_employees()
result = QuickRestoClassGenerator("Employee", "", employees[0], set())

print(result.get())
