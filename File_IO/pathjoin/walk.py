import os

for (root,dirs,files) in os.walk('.', topdown=True):
    print(files)
