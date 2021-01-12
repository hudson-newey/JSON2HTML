import json
import sys
import os, re, os.path

class Program:
    buildDIR = "static/"

    def createHTMLOBJ(tag, contents):
        litteralTag = tag[0:tag.find(" "):]
        return "<" + tag + ">" + contents + "</" + litteralTag + ">"
    
    def deleteSubDIR(dirPath):
        for root, dirs, files in os.walk(dirPath):
            for file in files:
                os.remove(os.path.join(root, file))

    def writeToFile(filePath, contents):
        f = open(filePath, "a")
        f.write(contents)
        f.close()

    # [<EntryPoint>]
    if __name__ == "__main__":
        # delete all previously built files
        deleteSubDIR(buildDIR)

        # define json file to read
        jsonFile = json.loads(open(sys.argv[1]).read())

        # read json elements
        #parse CSS from JSON file
        for i in range(len(jsonFile["style"])):
            writeToFile(buildDIR + sys.argv[1][:-5:] + ".css", jsonFile["style"][i])

        # open HTML template
        writeToFile(buildDIR + sys.argv[1][:-5:] + ".html", "<html><link rel='stylesheet' href='" + sys.argv[1][:-5:] + ".css'>")

        # parse HTML from JSON file
        for i in range(len(jsonFile["html"])):
            HTMLToPush = ""

            # convert json elements into HTML elements
            HTMLTag = jsonFile["html"][i]

            if (jsonFile["html"][i][:1:] == "<"):
                writeToFile(buildDIR + sys.argv[1][:-5:] + ".html", HTMLTag)
            else:
                HTMLToPush += createHTMLOBJ(HTMLTag, jsonFile[HTMLTag])
                writeToFile(buildDIR + sys.argv[1][:-5:] + ".html", HTMLToPush)
        
        # close HTML template
        writeToFile(buildDIR + sys.argv[1][:-5:] + ".html", "</html>")
        
        pass
