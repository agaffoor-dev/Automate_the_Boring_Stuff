import re

pattern = re.compile(r'\[\[(.+)\]\]')

with open("test.txt", "r") as file:
    contents = file.read()

    matches = pattern.finditer(contents)

    for match in matches:
        fp = open(f'{match.group(1)}.md', 'x')
        fp.close()
