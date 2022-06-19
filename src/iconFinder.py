import json

from Cheese.resourceManager import ResMan

class IconFinder:
    def __init__(self):
        with open(ResMan.resources("iconDictionary.json"), "r") as f:
            self.dict = json.loads(f.read())

    def find(self, file):
        fileType = file.split(".")[-1]
        if (fileType in self.dict):
            return self.dict[fileType]
        else:
            return "unknownIcon.png"

    def refreshIcons(self, jsn):
        with open(ResMan.resources("iconDictionary.json"), "w") as f:
            f.write(json.dumps(jsn))
