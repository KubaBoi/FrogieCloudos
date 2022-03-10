#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import os
import io

from cheese.resourceManager import ResMan
from cheese.modules.cheeseController import CheeseController
from cheese.ErrorCodes import Error

from python.repositories.fileRepository import FileRepository
from python.models.file import File

#@controller /upload
class UploadController(CheeseController):

    #@post /file
    @staticmethod
    def uploadFile(server, path, auth):
        r, info = UploadController.deal_post_data(server)
        f = io.BytesIO()
        if r: 
            print(info)
            CheeseController.serveFile(server, "/reconnect.html")
        else:
            response = CheeseController.createResponse({"ERROR": "File was not uploaded :("}, 500)
            CheeseController.sendResponse(server, response)

    #METHODS

    @staticmethod
    def deal_post_data(server):
        ctype, pdict = cgi.parse_header(server.headers['Content-Type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        pdict['CONTENT-LENGTH'] = int(server.headers['Content-Length'])
        if ctype == 'multipart/form-data':
            form = cgi.FieldStorage( fp=server.rfile, headers=server.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':server.headers['Content-Type'], })
            try:
                if isinstance(form["file"], list):
                    for record in form["file"]:
                        UploadController.saveFile(record)
                else:
                    UploadController.saveFile(form["file"])
            except IOError:
                    return (False, "Can't create file to write, do you have permission to write?")
        return (True, "Files uploaded")

    @staticmethod
    def saveFile(fileForm):
        if (os.path.exists(f"{ResMan.web()}" + "/files/" + fileForm.filename)): return
        open(f"{ResMan.web()}" + "/files/" + fileForm.filename, "wb").write(fileForm.file.read())
        id = FileRepository.findNewId()
        fileRecord = File(
            id,
            fileForm.filename,
            os.path.getsize(f"{ResMan.web()}" + "/files/" + fileForm.filename),
            fileForm.filename.split(".")[-1].lower()
        )
        saved = FileRepository.save(fileRecord)