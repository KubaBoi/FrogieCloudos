#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseRepository import CheeseRepository

#@repository favorites
#@dbscheme (id, name, path)
#@dbmodel Favorites
class FavoritesRepository(CheeseRepository):



	#GENERATED METHODS

	#@query "select * from favorites;"
	#@return array
	@staticmethod
	def findAll():
		return CheeseRepository.findAll([])

	#@query "select * from favorites where id=:id;"
	#@return one
	@staticmethod
	def find(id):
		return CheeseRepository.find([id])

	#@query "select * from favorites where :columnName=:value;"
	#@return array
	@staticmethod
	def findBy(columnName, value):
		return CheeseRepository.findBy([columnName, value])

	@staticmethod
	def findNewId():
		return CheeseRepository.findNewId([])+1

	@staticmethod
	def save(obj):
		return CheeseRepository.save([obj])

	@staticmethod
	def update(obj):
		return CheeseRepository.update([obj])

	@staticmethod
	def delete(obj):
		return CheeseRepository.delete([obj])

