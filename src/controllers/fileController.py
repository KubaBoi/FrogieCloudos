#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import shutil
from send2trash import send2trash

from Cheese.resourceManager import ResMan
from Cheese.cheeseController import CheeseController as cc
from Cheese.httpClientErrors import *
from Cheese.Logger import Logger



#@controller /file;
class FileController(cc):

    #@get /download;
    @staticmethod
    def download(server, path, auth):
        args = cc.getArgs(path)

        cc.checkJson(["file"], args)

        file = args["file"]

        if (platform.system() == "Windows"):
            file = file.replace("/", "\\")
        else:
            file = file.replace("\\", "/")

        if (not os.path.exists(file)):
            raise NotFound("File not found")

        Logger.info(f"Serving file: {file}")
        with open(file, "r") as f:
            data = f.read()

        return (data, 200)

    #@post /upload;
    @staticmethod
    def upload(server, path, auth):
        file = cc.readBytes(server)
        args = cc.getArgs(path)

        cc.checkJson(["name", "path"], args)

        name = args["name"]
        pth = args["path"]

        with open(os.path.join(pth, name), "wb") as f:
            f.write(file)

        return cc.createResponse({"STATUS": "File was uploaded"}, 200)

    #@post /copy;
    @staticmethod
    def copy(server, path, auth):
        args = cc.readArgs(server)

        cc.checkJson(["PATH", "ITEMS"], args)

        folder = args["PATH"]
        items = args["ITEMS"]

        if (not os.path.exists(folder)):
            raise NotFound("Folder not found")

        for item in items:
            if (os.path.isfile(item)):
                shutil.copy2(item, folder)
            elif (os.path.isdir(item)):
                shutil.copytree(item, os.path.join(folder, ResMan.getFileName(item)))

        return cc.createResponse({"STATUS": "ok"}, 200)

    #@post /move;
    @staticmethod
    def move(server, path, auth):
        args = cc.readArgs(server)

        cc.checkJson(["PATH", "ITEMS"], args)

        folder = args["PATH"]
        items = args["ITEMS"]

        if (not os.path.exists(folder)):
            raise NotFound("Folder not found")

        for item in items:
            if (os.path.isfile(item)):
                shutil.copy2(item, folder)
                if (os.path.exists(os.path.join(folder, ResMan.getFileName(item)))):
                    os.remove(item)
            elif (os.path.isdir(item)):
                shutil.copytree(item, os.path.join(folder, ResMan.getFileName(item)))
                if (os.path.exists(os.path.join(folder, ResMan.getFileName(item)))):
                    shutil.rmtree(item, onerror=FileController.onerror)

        return cc.createResponse({"STATUS": "ok"}, 200)

    #@post /remove;
    @staticmethod
    def remove(server, path, auth):
        args = cc.readArgs(server)

        cc.checkJson(["PATH", "FILES"], args)

        files = args["FILES"]
        path = args["PATH"]

        for file in files:
            send2trash(file)

        return cc.createResponse({"STATUS": "ok"}, 200)

    #@get /rename;
    @staticmethod
    def rename(server, path, auth):
        args = cc.getArgs(path)

        cc.checkJson(["path", "newName"], args)

        file = args["path"]
        newName = args["newName"]

        if (not os.path.exists(file)):
            raise NotFound("File not found")

        os.rename(file, os.path.join(*file.split("\\")[:-1], newName).replace("C:", "C:\\"))

        return cc.createResponse({"STATUS": "ok"}, 200)

    #@get /mkdir;
    @staticmethod
    def mkdir(server, path, auth):
        args = cc.getArgs(path)

        cc.checkJson(["path"], args)

        folder = args["path"]

        if (not os.path.exists(folder)):
            raise NotFound("Folder not found")

        folderName = "New folder"
        actFolderName = folderName
        id = 0
        while (os.path.exists(os.path.join(folder, actFolderName))):
            id += 1
            actFolderName = f"{folderName} ({str(id)})"

        os.mkdir(os.path.join(folder, actFolderName))

        return cc.createResponse({"FOLDER": actFolderName}, 200)

    #@get /write;
    @staticmethod
    def write(server, path, auth):
        args = cc.getArgs(path)

        cc.checkJson(["path"], args)

        folder = args["path"]

        if (not os.path.exists(folder)):
            raise NotFound("Folder not found")

        folderName = "New file"
        actFolderName = folderName + ".txt"
        id = 0
        while (os.path.exists(os.path.join(folder, actFolderName))):
            id += 1
            actFolderName = f"{folderName} ({str(id)}).txt"

        open(os.path.join(folder, actFolderName), "w")

        return cc.createResponse({"FILE": actFolderName}, 200)



# METHODS

    @staticmethod
    def onerror(func, path, exc_info):
        import stat
        # Is the error an access error?
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
            func(path)
        else:
            raise

