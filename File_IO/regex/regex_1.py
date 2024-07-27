import re

#urls = '''
#https://www.google.com
#http://coreyms.com
#https://youtube.com
#https://www.nasa.gov
#'''

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

#subbed_urls = pattern.sub(r'\2\3', urls)

#print(subbed_urls)

with open("sample.txt", "r") as file:
    contents = file.read()

    matches = pattern.findall(contents)

    for match in matches:
        print(match)
