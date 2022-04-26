import json
import os

from PIL import Image

import win32ui
import win32gui
import win32con
import win32api

from cheese.resourceManager import ResMan

class IconFinder:
    def __init__(self):
        with open(f"{ResMan.resources()}/iconDictionary.json", "r") as f:
            self.dict = json.loads(f.read())

    def find(self, file):
        fileType = file.split(".")[-1]
        iconName = ""
        if (fileType in self.dict):
            iconName = self.dict[fileType]
        else:
            return "unknownIcon.png"

        if (iconName == "exeIcon.png"):
            try:
                iconName = self.findExe(file)
            except:
                iconName = iconName

        return iconName

    def findExe(self, file):
        iconPath = os.path.join("exes", ResMan.getFileName(file) + ".png")
        absPath = os.path.join(ResMan.web(), "images", iconPath)

        if (os.path.exists(absPath)):
            return iconPath

        ico_x = win32api.GetSystemMetrics(win32con.SM_CXICON)

        large, small = win32gui.ExtractIconEx(file,0)
        win32gui.DestroyIcon(small[0])

        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, ico_x, ico_x)
        hdc = hdc.CreateCompatibleDC()

        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0,0), large[0])

        hbmp.SaveBitmapFile( hdc, absPath)

        img = Image.open(absPath)

        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            if (item[0] == 0 and item[1] == 0 and item[2] == 0):
                newData.append((0, 0, 0, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(absPath, "PNG")

        return iconPath