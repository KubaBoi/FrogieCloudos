#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import inspect

from cheese.resourceManager import ResMan
from cheese.databaseControll.database import Database

#REPOSITORIES
from cheese.repositories.favoritesRepositoryImpl import FavoritesRepositoryImpl


"""
File generated by Cheese Framework

Database query of Cheese Application
"""

class CheeseRepository:

    @staticmethod
    def findAll(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.findAll(args)
    @staticmethod
    def find(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.find(args)
    @staticmethod
    def findBy(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.findBy(args)
    @staticmethod
    def findNewId(args):
        userRepository = CheeseRepository.findUserRepository()
        args = CheeseRepository.getTypeOf(args)

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.findNewId(args)


    @staticmethod
    def save(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.save(args)
    @staticmethod
    def update(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.update(args)
    @staticmethod
    def delete(args):
        userRepository = CheeseRepository.findUserRepository()

        if (userRepository == "favoritesRepository"):
            return FavoritesRepositoryImpl.delete(args)


    @staticmethod
    def initRepositories():
        FavoritesRepositoryImpl.init()

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
            if (type(arg) is str):
                if (len(arg) == 0): newArgs.append("")
                elif (arg[-1] != "\'" 
                    and arg[-1] != ")" 
                    and not arg.endswith("DESC") 
                    and not arg.endswith("ASC")):
                    if (arg.startswith("columnName-")):
                        newArgs.append(arg.replace("columnName-", ""))
                    else:
                        newArgs.append(f"\'{arg}\'")
                else:
                    newArgs.append(str(arg))
            elif (type(arg) is list):
                newArgs.append("(" + ",".join(CheeseRepository.getTypeOf(arg)) + ")")
            elif (type(arg) is datetime):
                newArgs.append("'" + datetime.strftime(arg, "%d-%m-%Y %H:%M:%S") + "'")
            else:
                newArgs.append(str(arg))
        return newArgs

