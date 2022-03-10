#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cheese.modules.cheeseModel import CheeseModel

#@model
class File(CheeseModel):

    def __init__(self, id=None, file_name=None, file_size=None, file_type=None):
        self.id = id
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type

    def toJson(self):
        response = {
            "ID": self.id,
            "FILE_NAME": self.file_name,
            "FILE_SIZE": self.file_size,
            "FILE_TYPE": self.file_type
        }
        return response