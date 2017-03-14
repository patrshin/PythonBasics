import os
import sys
import re
import fileinput
path = "E:\\User\\Documents\\GitHub\\pythonParse"
regex = re.compile("(Sikorsky Aircrafts) (\d{4})")
def parseAndReplace(filePath):
    textFile = open(filePath, 'r')
    for line in textFile:
        if (regex.search(line)):
            a = re.sub("(Sikorsky Aircrafts) (\d{4})", 'Lockheed Martin', line)
            print(line, ' ', a)

for root, dirs, files in os.walk(path):
    path = root.split(os.sep)
    print((len(path) - 1) * '-', root)
    ##for dir in dirs:
        ##//print (dir)
    for fileName in files:
        if (fileName.endswith('.txt')):
            print(len(path) * '-', fileName)
            parseAndReplace(root + "\\" + fileName);
