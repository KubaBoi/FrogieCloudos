from urllib.parse import unquote
from cheese.modules.cheeseController import CheeseController

#@authorization disabled
class Authorization:

    @staticmethod
    def authorize(server, path, method):
        print(path, method)