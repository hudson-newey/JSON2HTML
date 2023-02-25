import json
import sys

from util.util import printHelpDocs, deleteSubDIR, createDirectory, doesDirectoryExist, writeToFile
from util.constants import BUILD_DIRECTORY, BUILD_PATH

def createHTMLOBJ(tag, contents):
    literalTag = tag[0:tag.find(" ") if " " in tag else len(tag):]
    return f"<{tag}>{contents}</{literalTag}>"

# program entry point
if __name__ == "__main__":
    # check that the program was called correctly
    if len(sys.argv) < 2:
        printHelpDocs()

    # delete all previously built files
    deleteSubDIR(BUILD_PATH)

    # define json file to read
    jsonFile = json.loads(open(sys.argv[1]).read())
    outFile = BUILD_PATH + sys.argv[1][:-5:]

    # check that the static directory exists
    if not doesDirectoryExist(BUILD_DIRECTORY):
        createDirectory(BUILD_DIRECTORY)

    # read json elements
    #parse CSS from JSON file
    if "style" in jsonFile:
        for cssLine in jsonFile["style"]:
            writeToFile(f"{outFile}.css", cssLine)

        # open HTML template
        writeToFile(f"{outFile}.html", f"<html><link rel='stylesheet' href='{sys.argv[1][:-5:]}.css'>")
        print(f"Created File {sys.argv[1][:-5:]}.css as target.")
    else:
        writeToFile(f"{outFile}.html", "<html>")

    # parse JS from JSON file
    if "script" in jsonFile:
        for jsLine in jsonFile["script"]:
            writeToFile(f"{outFile}.js", jsLine)

        # open HTML template
        writeToFile(f"{outFile}.html", f"<script src='{sys.argv[1][:-5:]}.js' defer></script>")
        print(f"Created File {sys.argv[1][:-5:]}.js as target.")

    # parse HTML from JSON file
    if "html" in jsonFile:
        for i in range(len(jsonFile["html"])):
            HTMLToPush = ""

            # convert json elements into HTML elements
            HTMLTag = jsonFile["html"][i]

            if jsonFile["html"][i][:1:] == "<":
                writeToFile(f"{outFile}.html", HTMLTag)
            else:
                htmlTagContents = ""
                if HTMLTag in jsonFile:
                    htmlTagContents = jsonFile[HTMLTag]

                HTMLToPush += createHTMLOBJ(HTMLTag, htmlTagContents)
                writeToFile(f"{outFile}.html", HTMLToPush)

        # close HTML template
        writeToFile(f"{outFile}.html", "</html>")

        print(f"Created File {outFile}.html as target.")
