from urllib.parse import unquote
from cheese.modules.cheeseController import CheeseController

#@authorization enabled
class Authorization:

    @staticmethod
    def authorize(server, path, method):
        splited = path.split("/")
        if (len(splited) < 3): return None
        if (splited[2] == "delete"):
            return {
                "file": splited[3]
            }
        return None