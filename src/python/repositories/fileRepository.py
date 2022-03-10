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

    #@query "select * from files where file_name=:fileName;"
    #@return one
    @staticmethod
    def findFileByName(fileName):
        return CheeseRepository.findFileByName([fileName])

    #@commit "delete from files where id=:id;"
    @staticmethod
    def deleteFile(id):
        return CheeseRepository.deleteFile([id])

    @staticmethod
    def save(obj):
        return CheeseRepository.save([obj])

    @staticmethod
    def update(obj):
        return CheeseRepository.update([obj])
