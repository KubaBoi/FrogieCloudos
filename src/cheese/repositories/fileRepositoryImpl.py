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
        if (type(var) is int):
            var = int(var)
        elif (type(var) is float):
            var = float(var)
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
            db = Database()
            response = db.query(f"select {FileRepositoryImpl.schemeNoBrackets} from files;")
            db.done()
        except Exception as e:
            Logger.fail("An error occurred while query request", str(e))

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
            db = Database()
            response = db.query(f"select {FileRepositoryImpl.schemeNoBrackets} from files where file_name={fileName} order by id ASC;")
            db.done()
        except Exception as e:
            Logger.fail("An error occurred while query request", str(e))

        if (response == None): return response
        if (len(response) > 0):
            return FileRepositoryImpl.toModel(response[0])
        else: return None

    @staticmethod
    def findNewId(args):

        response = None
        try:
            db = Database()
            response = db.query(f"select max(id) from files;")
            db.done()
        except Exception as e:
            Logger.fail("An error occurred while query request", str(e))

        if (response == None): return response
        return int(response[0][0])

    @staticmethod
    def updateId(args):
        id = args[0]
        file_name = args[1]

        try:
            db = Database()
            db.commit(f"update files set id={id} where file_name={file_name};")
            db.done()
            return True
        except Exception as e:
            Logger.fail("An error occurred while commit request", str(e))
            return False

    @staticmethod
    def save(args):
        obj = FileRepositoryImpl.fromModel(args[0])

        try:
            db = Database()
            db.commit(f"insert into {FileRepositoryImpl.table} {FileRepositoryImpl.scheme} values {obj};")
            db.done()
            return True
        except Exception as e:
            Logger.fail("An error occurred while commit request", str(e))
            return False

    @staticmethod
    def update(args):
        obj = FileRepositoryImpl.fromModel(args[0])

        try:
            db = Database()
            db.commit(f"update {FileRepositoryImpl.table} set {FileRepositoryImpl.scheme} = {obj} where id={obj[0]};")
            db.done()
            return True
        except Exception as e:
            Logger.fail("An error occurred while commit request", str(e))
            return False

    @staticmethod
    def delete(args):
        obj = FileRepositoryImpl.fromModel(args[0])

        try:
            db = Database()
            db.commit(f"delete from {FileRepositoryImpl.table} where id={obj[0]};")
            db.done()
            return True
        except Exception as e:
            Logger.fail("An error occurred while commit request", str(e))
            return False

