from quick_resto_api import QuickRestoApi
from quick_resto_objects.quick_resto_object import QuickRestoObject


class OperationsWithObjects:
    def __init__(self, quick_resto_api: QuickRestoApi):
        self._api: QuickRestoApi = quick_resto_api

    def getList(self, moduleName: str, ownerContextId: int = None,
                ownerContextClassName: str = None, showDeleted: bool = False):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "showDeleted": showDeleted
        }

        return self._api.get("/api/list", parameters=params)

    def getTree(self, moduleName: str, ownerContextId: int = None,
                ownerContextClassName: str = None, showDeleted: bool = False):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "showDeleted": showDeleted
        }

        return self._api.get("/api/tree", parameters=params)

    def getObject(self, moduleName: str, objectId: int, objectRid: int = None):
        params = {
            "moduleName": moduleName,
            "objectId": objectId,
            "objectRid": objectRid
        }

        return self._api.get("/api/get", parameters=params)

    def getObjectWithSubobjects(self, moduleName: str, objectId: int, objectRid: int = None):
        params = {
            "moduleName": moduleName,
            "objectId": objectId,
            "objectRid": objectRid
        }

        return self._api.get("/api/read", parameters=params)

    def createObject(self, object: QuickRestoObject, moduleName: str, ownerContextId: int = None,
                     ownerContextClassName: str = None, parentContextId: int = None,
                     parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.get_json_object()

        return self._api.post("/api/create", parameters=params, json_data=json_data)

    def updateObject(self, object: QuickRestoObject, moduleName: str, ownerContextId: int = None,
                     ownerContextClassName: str = None, parentContextId: int = None,
                     parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.get_json_object()

        return self._api.post("/api/update", parameters=params, json_data=json_data)

    def removeObject(self, object: QuickRestoObject, moduleName: str, ownerContextId: int = None,
                     ownerContextClassName: str = None, parentContextId: int = None,
                     parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.get_json_object()

        return self._api.post("/api/remove", parameters=params, json_data=json_data)

    def recoverObject(self, object: QuickRestoObject, moduleName: str, ownerContextId: int = None,
                      ownerContextClassName: str = None, parentContextId: int = None,
                      parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.get_json_object()

        return self._api.post("/api/recover", parameters=params, json_data=json_data)
