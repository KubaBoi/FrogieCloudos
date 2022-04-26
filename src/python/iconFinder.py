import json

from cheese.resourceManager import ResMan

class IconFinder:
    def __init__(self):
        with open(f"{ResMan.resources()}/iconDictionary.json", "r") as f:
            self.dict = json.loads(f.read())

    def find(self, file):
        fileType = file.split(".")[-1]
        if (fileType in self.dict):
            return self.dict[fileType]
        else:
            return "unknownIcon.png"
