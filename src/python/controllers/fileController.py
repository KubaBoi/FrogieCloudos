#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import os

from cheese.resourceManager import ResMan
from cheese.modules.cheeseController import CheeseController
from cheese.ErrorCodes import Error

from python.repositories.fileRepository import FileRepository
from python.iconFinder import IconFinder

#@controller /fileController
class FileController(CheeseController):

    #@post /getFiles
    @staticmethod
    def getFiles(server, path, auth):
        files = FileRepository.findFiles()
        data = []
        iconFinder = IconFinder()
        for f in files:
            if (not os.path.exists(f"{ResMan.web()}/files/{f.file_name}")):
                deleted = FileRepository.deleteFile(f.id)
                continue
            
            data.append(
                    {
                        "filename": f.file_name,
                        "size": FileController.convertBytes(f.file_size),
                        "byteSize": f.file_size,
                        "type": iconFinder.find(f.file_type),
                        "realType": f.file_type,
                        "date": os.path.getatime(f"{ResMan.web()}/files/{f.file_name}")
                    }
                )

        response = CheeseController.createResponse({"FILES": data}, 200)
        CheeseController.sendResponse(server, response)

    #@post /delete
    @staticmethod
    def removeFile(server, path, auth):
        fileName = auth["args"]["FILE_NAME"]

        file = FileRepository.findFileByName(fileName)
        if (file == None):
            CheeseController.sendResponse(server, Error.FileNotFound)
        else:
            deleted = FileRepository.deleteFile(file.id)
            if (not deleted):
                response = CheeseController.createResponse({"ERROR": "File was not removed :("}, 500)
                CheeseController.sendResponse(server, response)
            else:
                os.remove(f"{ResMan.web()}/files/{fileName}")
                response = CheeseController.createResponse({"OK": "OK"}, 200)
                CheeseController.sendResponse(server, response)

    #METHODS

    @staticmethod
    def convertBytes(bytes):
        if bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(bytes, 1024)))
        p = math.pow(1024, i)
        s = round(bytes / p, 2)
        return "%s %s" % (s, size_name[i])