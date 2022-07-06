import sys
from quick_resto_interface import *

interface = QuickRestoInterface(sys.argv[1], sys.argv[2], True, "quickresto.ru")

someDict = {
        "some": 1321,
        "someA": {
            "another": {
                "nestednestedObj": 214,
            },
            "nestedSome": "214",
            "anotherNestedSome": {
                "nestednestedObj": "reag",
                "aevr": [
                        {
                        "rebr": 214,
                        "raeb": 214,
                        }, 
                        {
                        "rebr": 214,
                        },
                ]
            },
            "erbs": "erq",
        },
        "lastSome": "last",
    }

anotherDict = [
    {
        "eqwv": 214,
        "qewvr": "erq",
    },
    {
        "DVSA": 3223,
        "REB": "REQH",
    },
]

print(interface.convert_to_csv(someDict))