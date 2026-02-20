print('correct file')

s1 = 'meow'
s2 = 'meowoeew'
print(s1, s2)

import math
# f string f'{value: command}'
print(f'{1e6 * math.pi:e}') # scientific notation
print(f'{"hello":.>20}') # move to right by 20 characters with . filler

# seq[0]= first letter, seq[1]= second, seq[-1]= last (count backwards)
seq = 'GAATTC' 
for nt in seq:
    print(nt, end='') # end='' prints with no spaces, without prints with return after ea
print() # presses enter after printing

# prints numbers counting each character
for i in range(len(seq)): # range(len(seq)) goes through every char bc start at 0
    print(i, seq[i]) # gives 1 G 2 A etc.

# slices: s[start : stop before : step size]
s = 'ABCDEFGHIJ'
print(s[0:5]) # start at 0 end before 5 
print(s[0:8:2]) # start at 0 end before 8 step size 2 
print(s[0:5], s[:5]) # same
print(s[5:len(s)], s[5:]) # same 

# s[::] = whole string, s[0:len(s)] = whole string, s[::-1] = whole string reversed

dna = 'ATGCTGTAA'
for i in range(0,len(dna),3):
    codon = dna[i:i+3]
    print(i, codon)

nts = 'ACGT'
for i in range(len(nts)):
    print(i, nts[i])
# enumerate orders with numbers (tuple)
for i, nt in enumerate(nts):
    print(i, nt)

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])

# zip pairs up nts and names in tuples
for nt, name in zip(nts, names):
    print(nt, name)

# zip and enumerate pairs up and adds numbers in order gives tuples
for i, (nt, name) in enumerate(zip(nts, names)):
    print(i, nt, name)

# lists= like tuple but [] and mutable 
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G' # replace 2 with G
print(nts)
nts.append('C') #append adds to list
print(nts) # ATGC
last = nts.pop() # list.pop() gives u last item in list (C)
print(last) # list.pop(0) removes first 
nts.sort() # sort alphabetical
print(nts)
nts.sort(reverse=True) #sort in reverse
print(nts)

nucleotides = nts # append affects both 
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list() is empty list, can append to add stuff
# list() can convert string to list of letters
alph = 'ABCDEFGHIJKLMNOPQRSTUVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day        to you'
words = text.split() # split into individual words
print(words)

# tsv or csv data need to be split with comma or \t
line = '1.41, 2.72, 3.14'
print(line.split(',')) 

s = '-'.join(aas) # sep by dashes
print(s)
s = ''.join(aas) # not sep
print(s)

# searching with if 
if 'A' in alph: print('yay :3')
if 'a' in alph: print('no')

print('index G?', alph.index('G')) # index returns error if can't find
print('find G?', alph.find('G')) # find returns -1 if can't find

# Write a function that returns the minimum value of a list.
numberss = [2,3,4,1]
def min_value(lst):
    smallest =lst[0]
    for item in lst: 
        if item < smallest: 
            smallest = item
    return smallest
print(min_value(numberss))

# Write a function that returns both the minimum and maximum values of a list.
def minmax(lst):
    mini = lst[0]
    maxi = lst[0]
    for item in lst:
        if item < mini: mini = item
        if item > maxi: maxi = item
    return mini, maxi
print(minmax(numberss)) 

# Write a function that returns the mean of the values in a list.
def mean(lst):
    total = 0
    for item in lst: 
        total += item
    return total/ len(numberss)
print(mean(numberss))

# Write a function that computes the entropy of a probability distribution. entropy H = Σ -p log2(p)
def entropy(vaomatua):
    H = 0
    for P in vaomatua:
        H -= P * math.log2(P)
    return H 
print(entropy([0.2, 0.3, 0.5]))

# Write a function manhattan(X1, X2) that computes the Manhattan distance between two lists of numbers.

def manhattan(X1, X2):
    distance = 0
    for x1, x2 in zip(X1, X2):
            distance += abs(x1 - x2)
    return distance

a = [0.25, 0.25, 0.25, 0.25]
b = [0.4, 0.3, 0.2, 0.1]

print(manhattan(a, b))

# Write a function dkl(P, Q) that computes the Kullback-Leibler distance between two histograms. 
# You should check that P and Q are actually histograms and you should do something about values of zero.

import math
import sys

def dkl(P, Q):
    if not math.isclose(1.0, sum(P)): sys.exit('error') # error if doesn't sum to 1 bc it's probability
    distance = 0
    for p, q in zip(P, Q):
        if p == 0: continue # skip zero
        if q == 0: continue
        distance = p * math.log2(p/q)
    return distance


a =[0.25, 0.25, 0.25, 0.25]
b =[0.25, 0.25, 0.25, 0.25]
print(dkl(a,b))

def pairwise_percent(s1, s2):
    diff = 0 # start at no differences
    for c1, c2 in zip(s1, s2):
        if c1 != c2: diff += 1 # if difference, add 1 to diff
    return 1- diff/len(s1)

s1 = 'ACGATATACAGTA'
s2 = 'ACGATAGACAGTA'

print(pairwise_percent(s1, s2))

def get_list_from_file(filename):
    strings =[]
    with open(filename) as fp:
        for line in fp:
            strings.append(line.strings())
    return strings

import sys

# def jaccard(f1, f2):
   # X1 = get_list_from_file(f1)
  #  X2 = get_list_from_file(f2)
    #unique_a = []
    #unique_b = []
    #shared = []
    #for x1 in X1:
  #      if x1 in X2: shared.append(x1)
  #      else: unique_a.append(x1)
  #  for x2 in X2:
   #     if x2 not in X1: unique_b.append(x2)
  #  print(unique_a)
  #  print(unique_b)
  #  print(shared)
    # return len(shared)/ len(shared) + len(unique_a) + len(unique_b)

# file1 = sys.argv[1]
# file2 = sys.argv[2]

# print(jaccard(file1, file2))

import sys

filename = sys.argv[1]
target_r = int(sys.argv[2])
target_g = int(sys.argv[3])
target_b = int(sys.argv[4])

with open(filename) as fp:
    for line in fp:
        colorname, hexvalue, rgbs = line.split()
        r, g, b = rgsb.split(',')
        distance = 0
        distance += abs(target_r - int(r))
        distance += abs(target_g - int(g))
        distance += abs(target_b - int(b))
       
# Write a function hydropathy(pro) that computes the average Kyte-Doolitle hydrophobicity
# of a protein sequence. Use the variables as defined below.

def kdh(seq):
    aas = 'ACDEFGHIKLMNPQRSTVWY'
    kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
    for aa in seq:
        print(aa)
    return -0.1
