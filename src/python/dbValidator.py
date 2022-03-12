
from distutils.log import Log
import os

from cheese.resourceManager import ResMan
from cheese.Logger import Logger

from python.repositories.fileRepository import FileRepository
from python.models.file import File

class DBV:

    @staticmethod
    def validate():
        Logger.bold("SYNCHRONIZING DB with files on server:")
        for root, dirs, files in os.walk(f"{ResMan.web()}/files"):
            id = 1
            notInDbFiles = []
            for name in files:
                if (name == ".gitignore"): continue
                file = FileRepository.findFileByName(name)
                if (file != None):
                    if (file.id != id):
                        file.id = id
                        if (FileRepository.save(file)):
                            Logger.okCyan(f"File {name}'s id was fixed")
                        else:
                            Logger.fail(f"Error while fixing {name}'s id")
                    else:
                        Logger.okGreen(f"File {name} was OK")
                else:
                    Logger.warning(f"File {name} was not in DB")
                    notInDbFiles.append(name)
                id += 1
            DBV.addMissingFiles(notInDbFiles)
            Logger.info("Synchronization DONE")

    @staticmethod
    def addMissingFiles(missingFiles):
        Logger.bold("Adding missing files")
        for file in missingFiles:
            fileObj = File()
            fileObj.id = FileRepository.findNewId() + 1
            fileObj.file_name = file
            fileObj.file_type = file.split(".")[-1].lower()
            fileObj.file_size = os.path.getsize(f"{ResMan.web()}/files/{file}")
            if (FileRepository.save(fileObj)):
                Logger.okGreen(f"File {file} added")
            else:
                Logger.fail(f"Error while adding {file}")