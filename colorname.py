# Write a program colorname.py <file> <R> <G> <B> that reports the closest 
# official HTML color name given some RGB values on the command line. 
# Data is in the colors_extended.tsv file.

import sys

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])
# print(filename)
min_distance = 1000
min_color = None 
with open(filename) as fp:
    for line in fp:
        colorname, hexvalue, rgbs = line.split()
        r, g, b = rgbs.split(',')
        distance = 0
        distance += abs(target_r - int(r))
        distance += abs(target_g - int(g))
        distance += abs(target_b - int(b))
        if distance < min_distance:
            min_distance = distance
            min_color = colorname 

       # print(colorname, distance)
print(min_color) 


import sys
filename = int(sys.argv[1])
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])
min_distance = 1000 #big number 
min_color = None 
with open(filename) as fp:
    for line in fp:
        colorname, hexvalue, rgbs = line.split() # split 3 lines from file
        r, g, b = rgbs.split() # split into 3 values that user can add
        distance = 0 # variable we want start at 0 distance
        distance += abs(target_r - int(r))
        distance += abs(target_g - int(g))
        distance += abs(target_b - int(b)) # user input - rgb value from file
        if distance < min_distance:
            min_distance = distance
            min_color = colorname 