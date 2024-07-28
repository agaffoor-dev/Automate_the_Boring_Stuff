import os
import shutil

path = os.getcwd()

file_list = os.listdir(path)

for file in file_list:
    if file.endswith('.jpg'):
        shutil.move(file, 'arranged/jpg')
    if file.endswith('.txt'):
        shutil.move(file, 'arranged/txt')
    if file.endswith('.pdf'):
        shutil.move(file, 'arranged/pdf')
