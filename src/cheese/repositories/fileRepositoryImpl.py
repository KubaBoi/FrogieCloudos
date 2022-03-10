#!/usr/bin/env python
# -*- coding: utf-8 -*-
#AUTOGENERATED FILE

from cheese.databaseControll.database import Database
from cheese.Logger import Logger
from python.models.file import File


class FileRepositoryImpl:

    @staticmethod
    def init():
        FileRepositoryImpl.table = "files"
        FileRepositoryImpl.scheme = "(id,file_name,file_size,file_type)"
        FileRepositoryImpl.schemeNoBrackets = "id,file_name,file_size,file_type"

    @staticmethod
    def convert(var):
        try:
            var = int(var)
        except:
            var = var
        return var

    @staticmethod
    def toJson(object):
        scheme = FileRepositoryImpl.schemeNoBrackets.split(",")
        ret = {}
        for s, o in zip(scheme, list(object)):
            try:
                ret[s] = int(o)
            except:
                ret[s] = o
        return ret

    @staticmethod
    def toModel(obj):
        model = File()
        model.id = FileRepositoryImpl.convert(obj[0])
        model.file_name = FileRepositoryImpl.convert(obj[1])
        model.file_size = FileRepositoryImpl.convert(obj[2])
        model.file_type = FileRepositoryImpl.convert(obj[3])
        return model

    @staticmethod
    def fromModel(model):
        tuple = (
            model.id,
            model.file_name,
            model.file_size,
            model.file_type
        )
        return tuple

    @staticmethod
    def findFiles(args):

        response = None
        try:
            response = Database.query(f"select {FileRepositoryImpl.schemeNoBrackets} from files;")
            Database.done()
        except Exception as e:
            Logger.fail(str(e))

        if (response == None): return response
        resp = []
        for a in response:
            resp.append(FileRepositoryImpl.toModel(a))
        return resp

    @staticmethod
    def findFileByName(args):
        fileName = args[0]

        response = None
        try:
            response = Database.query(f"select {FileRepositoryImpl.schemeNoBrackets} from files where file_name={fileName};")
            Database.done()
        except Exception as e:
            Logger.fail(str(e))

        if (response == None): return response
        if (len(response) > 0):
            return FileRepositoryImpl.toModel(response[0])
        else: return None

    @staticmethod
    def deleteFile(args):
        id = args[0]

        try:
            Database.commit(f"delete from files where id={id};")
            Database.done()
            return True
        except Exception as e:
            Logger.fail(str(e))
            return False

    @staticmethod
    def save(args):
        obj = FileRepositoryImpl.fromModel(args[0])

        try:
            Database.commit(f"insert into {FileRepositoryImpl.table} {FileRepositoryImpl.scheme} values {obj};")
            Database.done()
            return True
        except Exception as e:
            Logger.fail(str(e))
            return False

    @staticmethod
    def update(args):
        obj = FileRepositoryImpl.fromModel(args[0])

        try:
            Database.commit(f"update {FileRepositoryImpl.table} set {FileRepositoryImpl.scheme} = {obj} where id={obj[0]};")
            Database.done()
            return True
        except Exception as e:
            Logger.fail(str(e))
            return False

