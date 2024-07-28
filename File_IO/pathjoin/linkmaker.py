import os
import re

cwd = os.getcwd()

combined_text = []

pattern = re.compile(r'\[\[(.+)\]\]')

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r') as f:
                text = f.read()
                match = pattern.finditer(text)
                for x in match:
                    print(x.group(1))
#                    with open(f"{x.group(1)}", "a") as fi:
#                        fi.write("---\n" + f"up: [[\"{file}\"]]\n" + "---")
#                combined_text.append(text)

#string = " "
#string = string.join(combined_text)
#
#pattern = re.compile(r'\[\[(.+)\]\]')
#
#matches = pattern.finditer(string)
#
#for match in matches:
#    print(match.group(1))
