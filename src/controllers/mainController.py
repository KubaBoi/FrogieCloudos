#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Cheese.resourceManager import ResMan
from Cheese.appSettings import Settings
from Cheese.cheeseController import CheeseController as cc
from Cheese.httpClientErrors import *

from src.iconFinder import IconFinder

#@controller /main;
class MainController(cc):

	#@get /init;
	@staticmethod
	def init(server, path, auth):
		homeFolder = Settings.settings["initPath"]
		root = Settings.settings["root"]

		return cc.createResponse({"ROOT": root, "PATH": homeFolder}, 200)

	#@get /ls;
	@staticmethod
	def ls(server, path, auth):
		args = cc.getArgs(path)

		cc.checkJson(["path"], args)

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
			
		return cc.createResponse(jsonResponse, 200)

	#@get /exists;
	@staticmethod
	def exists(server, path, auth):
		args = cc.getArgs(path)

		cc.checkJson(["path"], args)

		file = args["path"]
		print(file)

		return cc.createResponse({'EXISTS': os.path.exists(file)}, 200)

	#TODO
	#@get /file;
	@staticmethod
	def file(server, path, auth):
		args = cc.getArgs(path)

		cc.checkJson(["path"], args)

		file = args["path"]

		return cc.createResponse({'FILE': {'NAME': 'str', 'CONTENT': 'str'}}, 200)

	# METHODS