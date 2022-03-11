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
        args = CheeseController.readArgs(server)
        try:
            if (method == "POST"):
                res = requests.post("http://localhost/authentication/authorizeToken", data=json.dumps(args))
                if (res.status_code != 200):
                    Logger.warning("Token was not authorized" + str(res.status_code))
                    return -1
        except:
            return -1

        return {
            "args": args,
            "pathArgs": pathArgs
        }