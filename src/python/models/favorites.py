#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseModel import CheeseModel

#@model
class Favorites(CheeseModel):
	def __init__(self, id=None, name=None, path=None):
		self.id=id
		self.name=name
		self.path=path

	def toJson(self):
		return {
			"ID": self.id,
			"NAME": self.name,
			"PATH": self.path
		}

	def toModel(self, json):
		self.id = json["ID"]
		self.name = json["NAME"]
		self.path = json["PATH"]
