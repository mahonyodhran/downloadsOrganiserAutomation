import os
import shutil

sourceDir = "C:/Users/odhra/Downloads/"
documentDir = "C:/Users/odhra/Documents/"
musicDir = "C:/Users/odhra/Music/"
pdfDir = "C:/Users/odhra/Documents/PDFs/"
imageDir = "C:/Users/odhra/Pictures/"
videoDir = "C:/Users/odhra/Videos/"

documentExtensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

musicExtensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

imageExtensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

videoExtensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

def checkDocument(name):
    for documentExtension in documentExtensions:
        if name.endswith(documentExtension) or name.endswith(documentExtension.upper()):
            shutil.move(sourceDir+name, documentDir)
            print(f"Moved document file: {name} to {documentDir}")
            
def checkMusic(name):
    for musicExtension in musicExtensions:
        if name.endswith(musicExtension) or name.endswith(musicExtension.upper()):
            shutil.move(sourceDir+name, musicDir)
            print(f"Moved music file: {name} to {musicDir}")
            
def checkImage(name):
    for imageExtension in imageExtensions:
        if name.endswith(imageExtension) or name.endswith(imageExtension.upper()):
            shutil.move(sourceDir+name, imageDir)
            print(f"Moved image file: {name} to {imageDir}")
            
def checkVideo(name):
    for videoExtension in videoExtensions:
        if name.endswith(videoExtension) or name.endswith(videoExtension.upper()):
            shutil.move(sourceDir+name, videoDir)
            print(f"Moved video file: {name} to {videoDir}")
            
def checkPDF(name):
    if name.endswith(".pdf") or name.endswith(".pdf".upper()):
        shutil.move(sourceDir+name, pdfDir)
        print(f"Moved PDF file: {name} to {pdfDir}")


with os.scandir(sourceDir) as entries:
    for entry in entries:
        name = entry.name
        checkMusic(name)
        checkDocument(name)
        checkImage(name)
        checkVideo(name)
            