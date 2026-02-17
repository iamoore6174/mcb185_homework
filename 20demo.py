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