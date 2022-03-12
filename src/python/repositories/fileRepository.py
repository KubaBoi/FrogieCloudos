#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseRepository import CheeseRepository

#@repository files
#@dbscheme (id, file_name, file_size, file_type)
#@dbmodel File
class FileRepository(CheeseRepository):

    #@query "select * from files;"
    #@return array
    @staticmethod
    def findFiles():
        return CheeseRepository.findFiles([])

    #@query "select * from files where file_name=:fileName order by id ASC;"
    #@return one
    @staticmethod
    def findFileByName(fileName):
        return CheeseRepository.findFileByName([fileName])

    #@query "select max(id) from files;"
    #@return num
    @staticmethod
    def findNewId():
        try:
            return CheeseRepository.findNewId([])
        except:
            return 0

    #@commit "update files set id=:id where file_name=:file_name;"
    @staticmethod
    def updateId(id, file_name):
        return CheeseRepository.updateId([id, file_name])

    @staticmethod
    def save(obj):
        return CheeseRepository.save([obj])

    @staticmethod
    def update(obj):
        return CheeseRepository.update([obj])

    @staticmethod
    def delete(obj):
        return CheeseRepository.delete([obj])
