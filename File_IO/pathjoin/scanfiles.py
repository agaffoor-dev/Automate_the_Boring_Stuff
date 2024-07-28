import os

path = os.getcwd()

objects = os.scandir(path)

for object in objects:
    if object.is_file():
        print(object.name)
