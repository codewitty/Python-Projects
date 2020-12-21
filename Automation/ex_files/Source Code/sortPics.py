import os
from pathlib import Path
from collections import Counter

SUBDIRECTORIES = {
    "jpeg": ['.JPG','.jpg'],
    "RAW":['.CR2','.CR3','.dng','.cr3'],
}

jpegList = []
rawList = []

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC' #If filetype doesn't exist in our dictionary


def createFileList(path,emptyList):
    for item in os.scandir(path):
        if item.is_dir():
            continue
        name = item.name
        new_name = name[:-4]
        print(new_name)
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
    

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

path = input("Enter source path\n")
organizeDirectory(path)
"""
jpegPath = input("Enter jpeg path\n")
createFileList(jpegPath, jpegList)
rawPath = input("Enter raw path\n")
createFileList(rawPath, rawList)
print(rawList)
print(jpegList)
deleteFile(rawPath,rawList,jpegList)
"""
