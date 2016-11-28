"""Script for combining downloaded Star Trek TNG epsiode scripts into single text file"""

import os
import glob

file_names = glob.glob("Scripts - TNG/*.txt")

tng = ""
for fn in file_names:
    with codecs.open(fn, "r", encoding='utf-8', errors='ignore') as f:
        tng += f.read()

new_lines = re.compile('\n{3,}')
tng = re.sub(new_lines, '\n\n', tng)

tng = re.sub(r'\x00', '', tng)
tng = re.sub(r'\x16', '', tng)

with open("star_trek.txt", "w") as f:
    f.write(tng)
