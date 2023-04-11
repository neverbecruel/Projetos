import os
import shutil

for item in os.listdir():
    if item.endswith(".pdf") or item.endswith(".doc") or item.endswith(".docx") or item.endswith(".xls"):
        shutil.move(item, 'ARQUIVOS')
    if item.endswith(".png") or item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".gif"):
        shutil.move(item, 'FOTOS')
    if item.endswith(".exe"):
        shutil.move(item, 'EXECUTAVEIS')
    if item.endswith(".mp3") or item.endswith(".wav"):
        shutil.move(item, 'AUDIO')
    if item.endswith(".mp4") or item.endswith(".avi") or item.endswith(".mkv"):
        shutil.move(item, 'VIDEO')
