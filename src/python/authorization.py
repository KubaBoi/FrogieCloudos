
from cheese.modules.cheeseController import CheeseController as cc
from cheese.appSettings import Settings

#@authorization enabled
class Authorization:

    @staticmethod
    def authorize(server, path, method):
        if (Authorization.isException(method, path)):
            return {"role": 0}

        if (method == "GET"):
            args = cc.getArgs(path)
            if (not cc.validateJson(["path"], args)):
                return {"role": 1}

            path = args["path"]
            if (not path.startswith(Settings.settings["root"])):
                return {"role": 1}

        elif (method == "POST"):
            args = cc.readArgs(server)
            if (not cc.validateJson(["PATH"], args)):
                return {"role": 1}

            path = args["PATH"]
            if (not path.startswith(Settings.settings["root"])):
                return {"role": 1}

        return {"role": 0}

    @staticmethod
    def isException(method, path):
        pathNoArgs = cc.getPath(path)

        for exception in Settings.authExcepts:
            if (exception["method"] == method):

                excpPath = exception["path"].replace("*", "")
                if (exception["path"].startswith("*")):
                    if (pathNoArgs.endswith(excpPath)): return True
                elif (exception["path"].endswith("*")):
                    if (pathNoArgs.startswith(excpPath)): return True
                else:
                    if (pathNoArgs == excpPath): return True

        return False