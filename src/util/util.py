import os, os.path

def printError(message = "Unknown Error..."):
    print(f"\nError: {message}")
    exit(2)

def deleteSubDIR(dirPath):
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            os.remove(os.path.join(root, file))

def writeToFile(filePath, contents):
    f = open(filePath, "a")
    f.write(contents)
    f.close()

def doesDirectoryExist(dirName):
    if dirName == None or dirName == "":
        printError("Directory name not specified in doesDirectoryExist() method...")

    return os.path.isdir(dirName)

def createDirectory(dirName):
    if dirName == None or dirName == "":
        printError("Directory name not specified in createDirectory() method...")

    if not os.path.exists(dirName):
        os.makedirs(dirName)

def printHelpDocs(shouldExit = True):
    from util.constants import HELP_MESSAGE

    print(HELP_MESSAGE)

    if shouldExit:
        printError("Bad usage...")
