import os
from pathlib import Path
from collections import Counter

jpegList = []
rawList = []

def getFileName(item):
    name = item.name
    filePath = Path(item)
    filetype = filePath.suffix.upper()
    new_name = name.replace(filetype,'')
    return new_name
    
def createFileList(path,emptyList):
    for item in os.scandir(path):
        if item.is_dir():
            continue
        fileName = getFileName(item)
        emptyList.append(fileName)


def deleteFile(rawPath,rawList,jpegList):
    res = list((Counter(rawList) - Counter(jpegList)).elements()) 
    for item in os.scandir(rawPath):
        if item.is_dir():
            continue
        raw_name = getFileName(item)
        if raw_name in res:
            os.remove(item)
    
jpegPath = input("Enter jpeg path\n")
createFileList(jpegPath, jpegList)
print(jpegList)
rawPath = input("Enter raw path\n")
createFileList(rawPath, rawList)
deleteFile(rawPath,rawList,jpegList)
