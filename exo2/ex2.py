#!/usr/bin/env
import re

with open("exo2.txt", "r") as file:
    txt = file.read()

rgx = re.compile(".* : \\{[^\\{]*\\}")
rgx_error = re.compile("mais ici c'est")
res = rgx.findall(txt)
errors = rgx_error.findall(txt)
for i in errors:
    if (i != None):
        print("Error in the file")

for i in res:
    print(i, end='')
print()