from urllib.parse import unquote
import requests
import json

from cheese.modules.cheeseController import CheeseController
from cheese.Logger import Logger

#@authorization enabled
class Authorization:

    @staticmethod
    def authorize(server, path, method):
        pathArgs = CheeseController.getArgs(server.path)
        try:
            if (method == "POST"):
                if (not CheeseController.validateJson(["token"], pathArgs)):
                    args = CheeseController.readArgs(server)
                else:
                    args = pathArgs
                    args["TOKEN"] = pathArgs["token"]

                args["ip"] = CheeseController.getClientAddress(server)
                res = requests.post("http://localhost/authentication/authorizeToken", data=json.dumps(args))

                if (res.status_code != 200):
                    return -1
            else:
                args = CheeseController.readArgs(server)
        except Exception as e:
            Logger.FAIL(str(e))
            return -1

        return {
            "args": args,
            "pathArgs": pathArgs
        }