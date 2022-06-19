#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import platform

from Cheese.resourceManager import ResMan
from Cheese.appSettings import Settings
from Cheese.cheeseController import CheeseController as cc
from Cheese.httpClientErrors import *
from Cheese.Logger import Logger

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

		if (platform.system() == "Windows"):
			file = file.replace("/", "\\")
		else:
			file = file.replace("\\", "/")

		return cc.createResponse({'EXISTS': os.path.exists(file)}, 200)

	#@post /syncIconJson;
	@staticmethod
	def syncIconJson(server, path, auth):
		args = cc.readArgs(server)

		cc.checkJson(["ICONS"], args)

		icon = IconFinder()
		icon.refreshIcons(args["ICONS"])

		return cc.createResponse({"STATUS": "OK"}, 200)

	#@post /syncIcons;
	@staticmethod
	def syncIcons(server, path, auth):
		file = cc.readBytes(server)
		args = cc.getArgs(path)

		cc.checkJson(["path"], args)

		# /images + pth
		pth = args["path"].replace("\\", "/")

		with open(ResMan.web('images', pth), "wb") as f:
			Logger.info(f"Saving: {ResMan.web('images', pth)}")
			f.write(file)

		return cc.createResponse({"STATUS": "File was uploaded"}, 200)

	#TODO
	#@get /file;
	@staticmethod
	def file(server, path, auth):
		args = cc.getArgs(path)

		cc.checkJson(["path"], args)

		file = args["path"]

		return cc.createResponse({'FILE': {'NAME': 'str', 'CONTENT': 'str'}}, 200)

	# METHODS
