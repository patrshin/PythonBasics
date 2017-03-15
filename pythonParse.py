import os
import sys
import re
import fileinput
import ctypes  # An included library with Python install.

path = "E:\\User\\Documents\\GitHub\\pythonBasics"
regex = re.compile("(Sikorsky Aircrafts) (\d{4})")
def parseAndReplace(filePath):
    #textFile = open(filePath)
    #outFile = open(filePath, 'w')
    with fileinput.input(filePath, inplace=True, backup= '.bak') as textFile:
        for line in textFile:
            ctypes.windll.user32.MessageBoxW(0, line, "Your title", 1)
            line = re.sub("(Sikorsky Aircrafts) (\d{4})", 'Lockheed Martin 2017', line.rstrip())
            ctypes.windll.user32.MessageBoxW(0, line, "Your title", 1)
            print (line)
            ##line.replace()

for root, dirs, files in os.walk(path):
    path = root.split(os.sep)
    print((len(path) - 1) * '-', root)
    ##for dir in dirs:
        ##//print (dir)
    for fileName in files:
        if (fileName.endswith('.txt')):
            print(len(path) * '-', fileName)
            parseAndReplace(root + "\\" + fileName);
