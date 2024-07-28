import os

print("Current Working Directory: ", os.getcwd())

os.makedirs('arranged', exist_ok=True)

os.chdir('arranged')

folder_list = ['pdf', 'jpg', 'txt']

for name in folder_list:
    os.makedirs(f"{name}")

print(os.getcwd())


