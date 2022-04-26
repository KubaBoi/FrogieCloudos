#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from cheese.ErrorCodes import Error
from cheese.resourceManager import ResMan
from cheese.appSettings import Settings
from cheese.modules.cheeseController import CheeseController as cc

from python.iconFinder import IconFinder

#@controller /main
class MainController(cc):

	#@get /init
	@staticmethod
	def init(server, path, auth):
		if (auth["role"] > 0):
			Error.sendCustomError(server, "Unauthorized", 401)
			return

		homeFolder = Settings.settings["initPath"]
		root = Settings.settings["root"]

		response = cc.createResponse({"ROOT": root, "PATH": homeFolder}, 200)
		cc.sendResponse(server, response)

	#@get /ls
	@staticmethod
	def ls(server, path, auth):
		if (auth["role"] > 0):
			Error.sendCustomError(server, "Unauthorized", 401)
			return

		args = cc.getArgs(path)

		if (not cc.validateJson(["path"], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		folder = args["path"]

		jsonResponse = {}
		jsonResponse["FOLDER"] = []

		icon = IconFinder()

		for root, dirs, files in os.walk(folder):
			for name in dirs:
					jsonResponse["FOLDER"].append(
					{
						"NAME": name,
						"IMAGE": "folder.png",
						"SIZE": "",
						"TYPE": "FOLDER"
					}
				)

			for name in files:
				jsonResponse["FOLDER"].append(
					{
						"NAME": name,
						"IMAGE": icon.find(os.path.join(root, name)),
						"SIZE": ResMan.convertBytes(os.path.getsize(os.path.join(root, name))),
						"TYPE": "FILE"
					}
				)
			break
			

		response = cc.createResponse(jsonResponse, 200)
		cc.sendResponse(server, response)

	#@get /exists
	@staticmethod
	def exists(server, path, auth):
		if (auth["role"] > 0):
			Error.sendCustomError(server, "Unauthorized", 401)
			return

		args = cc.getArgs(path)

		if (not cc.validateJson(["path"], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		file = args["path"]

		response = cc.createResponse({'EXISTS': os.path.exists(file)}, 200)
		cc.sendResponse(server, response)

	#TODO
	#@get /file
	@staticmethod
	def file(server, path, auth):
		if (auth["role"] > 0):
			Error.sendCustomError(server, "Unauthorized", 401)
			return

		args = cc.getArgs(path)

		if (not cc.validateJson(["path"], args)):
			Error.sendCustomError(server, "Wrong json structure", 400)
			return

		file = args["path"]

		response = cc.createResponse({'FILE': {'NAME': 'str', 'CONTENT': 'str'}}, 200)
		cc.sendResponse(server, response)

	# METHODS