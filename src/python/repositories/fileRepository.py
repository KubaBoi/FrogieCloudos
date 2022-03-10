#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseRepository import CheeseRepository

#@repository files
#@dbscheme (id, file_name, file_size, file_type)
#@dbmodel File
class FileRepository(CheeseRepository):

    #@query "select * from files;"
    #return array
    @staticmethod
    def findFiles():
        return CheeseRepository.findFiles([])