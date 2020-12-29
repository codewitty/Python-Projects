import os
from pathlib import Path

SUBDIRECTORIES = {
    "jpeg": ['.JPG','.jpg'],
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
        file_name = item.name
        if item.is_dir():
            print(item.path)
        else:
            print(file_name)

path = input("Enter path\n")
organizeDirectory(path)
