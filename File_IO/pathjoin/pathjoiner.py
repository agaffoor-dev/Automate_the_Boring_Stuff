import os

path = os.getcwd()
path_list = []
files = os.listdir(path)
print(files)
for file in files:
    path_list.append(os.path.join(path, file))
print(path_list)
