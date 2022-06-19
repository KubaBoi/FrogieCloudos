import json
import os

from Cheese.resourceManager import ResMan

class IconFinder:
    def __init__(self):
        with open(ResMan.resources("iconDictionary.json"), "r") as f:
            self.dict = json.loads(f.read())

    def find(self, file):
        fileType = file.split(".")[-1]
        iconName = ""
        if (fileType in self.dict):
            iconName = self.dict[fileType]
        else:
            return "unknownIcon.png"

        if (iconName == "exeIcon.png"):
            iconPath = os.path.join("exes", ResMan.getFileName(file) + ".png")
            absPath = ResMan.web("images", iconPath)

            if (os.path.exists(absPath)):
                return iconPath

        return iconName

    def refreshIcons(self, jsn):
        with open(ResMan.resources("iconDictionary.json"), "w") as f:
            f.write(json.dumps(jsn))
