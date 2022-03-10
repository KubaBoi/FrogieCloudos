#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect

from cheese.resourceManager import ResMan
from cheese.databaseControll.database import Database

#REPOSITORIES


"""
File generated by Cheese Framework

Database query of Cheese Application
"""

class CheeseRepository:





    @staticmethod
    def initRepositories():

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
                newArgs.append(f"\'{arg}\'")
            elif (type(arg) is list):
                newArgs.append("(" + ",".join(CheeseRepository.getTypeOf(arg)) + ")")
            else:
                newArgs.append(str(arg))
        return newArgs

