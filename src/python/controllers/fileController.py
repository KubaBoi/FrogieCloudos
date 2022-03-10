#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.resourceManager import ResMan
from cheese.modules.cheeseController import CheeseController
from cheese.ErrorCodes import Error

from python.repositories.fileRepository import FileRepository

#@controller /files
class FileController(CheeseController):

    #@get /getFiles
    @staticmethod
    def getFiles(server, path, auth):
        args = auth["args"]

        files = FileRepository.findFiles()
        print(files)

        response = CheeseController.createResponse({"OK": "OK"}, 200)
        CheeseController.sendResponse(server, response)