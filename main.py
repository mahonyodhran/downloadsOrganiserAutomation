import os

sourceDir = "C:/Users/odhra/Downloads"

with os.scandir(sourceDir) as entries:
    for entry in entries:
        print(entry)