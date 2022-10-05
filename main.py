import os
import shutil
from directories import book_dir, document_dir, image_dir, music_dir, pdf_dir, source_dir, sql_dir, video_dir
from extensions import book_extensions, document_extensions, image_extensions, music_extensions, video_extensions


def checkBook(name):
    for bookExtension in book_extensions:
        if name.endswith(bookExtension) or name.endswith(bookExtension.upper()):
            if(fileExists(book_dir, name)):
                print("File already exists - Skipping . .")
            else:
                shutil.move(source_dir+name, book_dir)
                print(f"Moved book file: {name} to {book_dir}")


def checkDocument(name):
    for documentExtension in document_extensions:
        if name.endswith(documentExtension) or name.endswith(documentExtension.upper()):
            if(fileExists(document_dir, name)):
                print("File already exists - Skipping . .")
            else:         
                shutil.move(source_dir+name, document_dir)
                print(f"Moved document file: {name} to {document_dir}")


def checkImage(name):
    for imageExtension in image_extensions:
        if name.endswith(imageExtension) or name.endswith(imageExtension.upper()):
            if(fileExists(image_dir, name)):
                print("File already exists - Skipping . .")
            else:
                shutil.move(source_dir+name, image_dir)
                print(f"Moved image file: {name} to {image_dir}")


def checkMusic(name):
    for musicExtension in music_extensions:
        if name.endswith(musicExtension) or name.endswith(musicExtension.upper()):
            if(fileExists(music_dir, name)):
                print("File already exists - Skipping . .")
            else:
                shutil.move(source_dir+name, music_dir)
                print(f"Moved music file: {name} to {music_dir}")


def checkPDF(name):
    if name.endswith(".pdf") or name.endswith(".pdf".upper()):
        if(fileExists(pdf_dir, name)):
            print("File already exists - Skipping . .")
        else:
            shutil.move(source_dir+name, pdf_dir)
            print(f"Moved PDF file: {name} to {pdf_dir}")


def checkVideo(name):
    for videoExtension in video_extensions:
        if name.endswith(videoExtension) or name.endswith(videoExtension.upper()):
            if(fileExists(video_dir, name)):
                print("File already exists - Skipping . .")
            else:
                shutil.move(source_dir+name, video_dir)
                print(f"Moved video file: {name} to {video_dir}")


def checkSQL(name):
    if name.endswith('sql'):
        if fileExists(sql_dir, name):
            print(f"File {name} exists - Skipping . .")
        else:
            shutil.move(source_dir+name, sql_dir)
            print(f"Moved video file: {name} to {sql_dir}")

def fileExists(directory ,name):
    return os.path.exists(directory + '/' + name)

with os.scandir(source_dir) as entries:
    for entry in entries:
        name = entry.name
        checkBook(name)
        checkDocument(name)
        checkImage(name)
        checkMusic(name)
        checkPDF(name)
        checkVideo(name)