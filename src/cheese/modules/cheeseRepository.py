#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect

from cheese.resourceManager import ResMan
from cheese.databaseControll.database import Database

#REPOSITORIES
from cheese.repositories.fileRepositoryImpl import FileRepositoryImpl


"""
File generated by Cheese Framework

Database query of Cheese Application
"""

class CheeseRepository:

    @staticmethod
    def findFiles(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.findFiles(args)
    @staticmethod
    def findFileByName(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.findFileByName(args)
    @staticmethod
    def findNewId(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.findNewId(args)


    @staticmethod
    def deleteFile(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.deleteFile(args)
    @staticmethod
    def updateId(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.updateId(args)
    @staticmethod
    def save(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.save(args)
    @staticmethod
    def update(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "fileRepository"):
            return FileRepositoryImpl.update(args)


    @staticmethod
    def initRepositories():
        FileRepositoryImpl.init()

        pass

    # finds name of user-made repository
    @staticmethod
    def findUserRepository():
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        userRepository = ResMan.getFileName(calframe[2][1]).replace(".py", "")
        return userRepository

    # convert arguments
    @staticmethod
    def getTypeOf(args):
        newArgs = []
        for arg in args:
            if (type(arg) is str and arg[-1] != "\'" 
                and arg[-1] != ")" 
                and not arg.endswith("DESC") 
                and not arg.endswith("ASC")):
                if (arg.startswith("columnName-")):
                    newArgs.append(arg.replace("columnName-", ""))
                else:
                    newArgs.append(f"\'{arg}\'")
            elif (type(arg) is list):
                newArgs.append("(" + ",".join(CheeseRepository.getTypeOf(arg)) + ")")
            else:
                newArgs.append(str(arg))
        return newArgs

