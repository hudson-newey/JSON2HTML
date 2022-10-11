import json
import sys

from util import *

BUILDDIR = "static/"

def createHTMLOBJ(tag, contents):
    litteralTag = tag[0:tag.find(" ") if " " in tag else len(tag):]
    return f"<{tag}>{contents}</{litteralTag}>"

# program entry point
if __name__ == "__main__":
    # check that the program was called correctly
    if len(sys.argv) < 2:
        printHelpDocs()

    # delete all previously built files
    deleteSubDIR(BUILDDIR)

    # define json file to read
    jsonFile = json.loads(open(sys.argv[1]).read())
    outFile = BUILDDIR + sys.argv[1][:-5:]

    # check that the static directory exists
    if not doesDirectoryExist("static"):
        createDirectory("static")

    # read json elements
    #parse CSS from JSON file
    if "style" in jsonFile:
        for i in range(len(jsonFile["style"])):
            writeToFile(f"{outFile}.css", jsonFile["style"][i])

        # open HTML template
        writeToFile(f"{outFile}.html", f"<html><link rel='stylesheet' href='{sys.argv[1][:-5:]}.css'>")
        print(f"Created File {sys.argv[1][:-5:]}.css as target.")

    # parse HTML from JSON file
    if "html" in jsonFile:
        for i in range(len(jsonFile["html"])):
            HTMLToPush = ""

            # convert json elements into HTML elements
            HTMLTag = jsonFile["html"][i]

            if jsonFile["html"][i][:1:] == "<":
                writeToFile(f"{outFile}.html", HTMLTag)
            else:
                HTMLToPush += createHTMLOBJ(HTMLTag, jsonFile[HTMLTag])
                writeToFile(f"{outFile}.html", HTMLToPush)
        
        # close HTML template
        writeToFile(f"{outFile}.html", "</html>")

        print(f"Created File {outFile}.html as target.")
