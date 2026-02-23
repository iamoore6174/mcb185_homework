# Write a function crazycase() that converts a a string into aLtErNaTiNg cAsE. 
# Use sys.argv to get the strings.

import sys 
import gzip 

def crazycase(s):
    result =''
    for i in range (len(s)):
        if i % 2 == 0:
            result += s[i].lower()
        else: 
            result += s[i].upper()
    return result 
filename = sys.argv[1]
with gzip.open(filename, 'rt') as fp:
    for line in fp:
        line = line.strip()

print(crazycase(line))

import sys

def crazycase(text):
    result = ''
    for i, char in enumerate(text):
        if i % 2 == 0:
            result += char.lower()
        else:
            result += char.upper()
    return result 

filename = sys.argv[1]

print(crazycase(word))

import sys
import gzip

def crazycase(text):
    result = ''
    for i in range (len(string)):
        if i % 2 == 0:
            result += string[i].lower()
        else: 
            result += string[i].upper()
    return result

filename = sys.argv[1]
with gzip.open(filename, 'rt') as fp:
    for line in fp:
        line = line.strip()