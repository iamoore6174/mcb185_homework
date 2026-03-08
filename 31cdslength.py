# Create a program called 31cdslength.py that reports the lengths of protein-coding genes in 
# the E. coli genome. The program will need to perform the following tasks as it reads 
# each line of the file.

# Skip over comment lines
# Find CDS features (or skip over all non-CDS features)
# Extract the begin and end coordinates
# Convert the coordinates to integers
# Report the length of the CDS (end - begin + 1)

import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg +1)

import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg +1)


import gzip
import sys

with gzip.open(sys.argv[1], 'rt'):
    for line in fp:
        if line[0] != '#':
            words = line.split()
            if words[2] == 'CDS':
                beg = int(words[3])
                end = int(words[4])
                print(end - beg +1)

import gzip
import sys

with gzip.open(sys.argv[1], 'rt'):
    for line in fp:
        if line[0] == '#': continue # if it's a comment, continue
        words = line.split()
        if words[2] != 'CDS': continue # if it's not CDS, continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg +1)