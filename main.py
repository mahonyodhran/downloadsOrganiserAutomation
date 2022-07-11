import os

sourceDir = "C:/Users/odhra/Downloads"
documentDir = "C:/Users/odhra/Documents"
musicDir = "C:/Users/odhra/Music"
imageDir = "C:/Users/odhra/Pictures"
videoDir = "C:/Users/odhra/Videos"

with os.scandir(sourceDir) as entries:
    for entry in entries:
        if("mp3" in entry.name):
            print(entry.name)