import os
from pathlib import Path

SUBDIRECTORIES = {
    "jpeg": ['.JPG','.jpg'],
    "HEIC": ['.heic', '.HEIC'],
    "MOV": ['.mov', '.MOV'],
    "RAW":['.CR2','.CR3','.dng','.cr3'],
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC' #If filetype doesn't exist in our dictionary

def organizeDirectory(path):
    for item in os.scandir(path):
        if item.is_dir():
            continue
        filePath = Path(item.path)
        fileType = filePath.suffix.lower()
        directory = pickDirectory(fileType)
        directoryp = os.path.join(path, directory)
        directoryPath = Path(directoryp)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        newpath = os.path.join(directoryp,item.name)
        filePath.rename(newpath)

path = input("Enter path\n")
organizeDirectory(path)
