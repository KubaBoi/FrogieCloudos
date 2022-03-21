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
                deleted = FileRepository.delete(f)
                continue
            
            data.append(
                    {
                        "filename": f.file_name,
                        "size": ResMan.convertBytes(f.file_size),
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
            deleted = FileRepository.delete(file)
            if (not deleted):
                response = CheeseController.createResponse({"ERROR": "File was not removed :("}, 500)
                CheeseController.sendResponse(server, response)
            else:
                os.remove(f"{ResMan.web()}/files/{fileName}")
                response = CheeseController.createResponse({"OK": "OK"}, 200)
                CheeseController.sendResponse(server, response)
