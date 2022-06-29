from quick_resto_api import QuickRestoApi
from quick_resto_objects.quick_resto_object import QuickRestoObject


class OperationsWithObjects:
    def getList(api: QuickRestoApi, moduleName: str, ownerContextId: int = None, 
                    ownerContextClassName: str = None, showDeleted: bool = False):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "showDeleted": showDeleted
        }

        return api.get("/api/list", parameters = params)

    def getTree(api: QuickRestoApi, moduleName: str, ownerContextId: int = None, 
                    ownerContextClassName: str = None, showDeleted: bool = False):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "showDeleted": showDeleted
        }

        return api.get("/api/tree", parameters = params)

    def getObject(api: QuickRestoApi, moduleName: str, objectId: int, objectRid: int = None):
        params = {
            "moduleName": moduleName,
            "objectId": objectId,
            "objectRid": objectRid
        }

        return api.get("/api/get", parameters = params)

    def getObjectWithSubobjects(api: QuickRestoApi, moduleName: str, objectId: int, objectRid: int = None):
        params = {
            "moduleName": moduleName,
            "objectId": objectId,
            "objectRid": objectRid
        }

        return api.get("/api/read", parameters = params)

    def createObject(api: QuickRestoApi, object: QuickRestoObject, moduleName: str, ownerContextId: int = None, 
                        ownerContextClassName: str = None, parentContextId: int = None, parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.__str__.__dict__

        return api.post("/api/create", parameters = params, json_data = json_data)

    def updateObject(api: QuickRestoApi, object: QuickRestoObject, moduleName: str, ownerContextId: int = None, 
                        ownerContextClassName: str = None, parentContextId: int = None, parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.__str__.__dict__

        return api.post("/api/update", parameters = params, json_data = json_data)

    def removeObject(api: QuickRestoApi, object: QuickRestoObject, moduleName: str, ownerContextId: int = None, 
                        ownerContextClassName: str = None, parentContextId: int = None, parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.__str__.__dict__

        return api.post("/api/remove", parameters = params, json_data = json_data)

    def recoverObject(api: QuickRestoApi, object: QuickRestoObject, moduleName: str, ownerContextId: int = None, 
                        ownerContextClassName: str = None, parentContextId: int = None, parentContextClassName: str = None):
        params = {
            "moduleName": moduleName,
            "ownerContextId": ownerContextId,
            "ownerContextClassName": ownerContextClassName,
            "parentContextId": parentContextId,
            "parentContextClassName": parentContextClassName
        }

        json_data = object.__str__.__dict__

        return api.post("/api/recover", parameters = params, json_data = json_data)