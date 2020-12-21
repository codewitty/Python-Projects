import os
from pathlib import Path
from collections import Counter

jpegList = []
rawList = []

def createFileList(path,emptyList):
    for item in os.scandir(path):
        if item.is_dir():
            continue
        name = item.name
        new_name = name[:-4]
        emptyList.append(new_name)


def deleteFile(rawPath,rawList,jpegList):
    res = list((Counter(rawList) - Counter(jpegList)).elements()) 
    print(res)
    for item in os.scandir(rawPath):
        if item.is_dir():
            continue
        name = item.name
        raw_name = name[:-4]
        if raw_name in res:
            os.remove(item)
    
jpegPath = input("Enter jpeg path\n")
createFileList(jpegPath, jpegList)
rawPath = input("Enter raw path\n")
createFileList(rawPath, rawList)
deleteFile(rawPath,rawList,jpegList)
