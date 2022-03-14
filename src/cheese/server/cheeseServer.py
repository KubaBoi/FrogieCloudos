#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn

from cheese.appSettings import Settings
from cheese.modules.cheeseController import CheeseController
from cheese.admin.adminManager import AdminManager
from cheese.Logger import Logger
from cheese.ErrorCodes import Error
from python.authorization import Authorization

#REST CONTROLLERS
from python.controllers.fileController import FileController
from python.controllers.uploadController import UploadController


"""
File generated by Cheese Framework

server handler of Cheese Application
"""

class CheeseServerMulti(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class CheeseServer(HTTPServer):
    """Handle requests in one thread."""

class CheeseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path.startswith("/admin")):
            AdminManager.controller(self)
            return
        self.__log()
        if (self.path == "/alive"):
            CheeseController.sendResponse(self, CheeseController.createResponse({"RESPONSE": "Yes"}, 200))
            return
        try:
            path = CheeseController.getPath(self.path)
            auth = Authorization.authorize(self, path, "GET")
            if (auth == -1): 
                CheeseController.sendResponse(self, Error.BadToken)
                return

            if (path == "/"):
                CheeseController.serveFile(self, "index.html")
            elif (path.startswith("/fileController")):
                pass
            elif (path.startswith("/upload")):
                pass
            else:
                CheeseController.serveFile(self, self.path)
        
        except Exception as e:
            Logger.fail("An error occurred", e)
            Error.sendCustomError(self, "Internal server error :(", 500)

    def do_POST(self):
        self.__log()
        try:
            auth = Authorization.authorize(self, self.path, "POST")
            if (auth == -1): 
                CheeseController.sendResponse(self, Error.BadToken)
                return

            if (self.path.startswith("/fileController")):
                if (self.path.startswith("/fileController/getFiles")):
                    FileController.getFiles(self, self.path, auth)
                elif (self.path.startswith("/fileController/delete")):
                    FileController.removeFile(self, self.path, auth)
                else:
                    Error.sendCustomError(self, "Endpoint not found :(", 404)
            elif (self.path.startswith("/upload")):
                if (self.path.startswith("/upload/file")):
                    UploadController.uploadFile(self, self.path, auth)
                else:
                    Error.sendCustomError(self, "Endpoint not found :(", 404)
            else:
                Error.sendCustomError(self, "Endpoint not found :(", 404)

        except Exception as e:
            Logger.fail("An error occurred", e)
            Error.sendCustomError(self, "Internal server error :(", 500)

    def end_headers(self):
        if (Settings.allowCORS):
            self.send_header("Access-Control-Allow-Origin", "*")
            BaseHTTPRequestHandler.end_headers(self)
        else:
            self.send_header("Content-type", "application/json")

    def log_message(self, format, *args):
        return

    def __log(self):
        Logger.okGreen(f"{self.client_address[0]} - {self.command} \"{self.path}\"")

