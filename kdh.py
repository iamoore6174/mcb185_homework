# Write a function hydropathy(pro) that computes the average Kyte-Doolitle hydrophobicity
# of a protein sequence. Use the variables as defined below.

def hydropathy(seq):
    aas = 'ACDEFGHIKLMNPQRSTVWY'
    kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
    total = 0
    for aa in seq:
        idx = aas.index(aa)
        total += kdh[idx]
    return total/ len(seq)

print(hydropathy('M'))

import sys
import itertools

def translate(orf):
    codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
    trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'
    prot = ''
    for i in range(0, len(orf), 3):
        codon = orf[i:i+3]
        idx = codons.index(codon)
        aa = trans[idx]
        prot += aa

    return prot

protein = translate('ATAGCGAAT') 
print(protein)

import random 

def random_subseq(seq, n, k): # n how many, k length
    subs = []
    for _ in range(n):
        x = random.randint(0, len(seq)-k)
        subseq = seq[x:x+k]
        subs.append(subseq)

    return subs

seq = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
subseqs = random_subseq(seq, 5, 7)
print(subseqs)

# Write a function anti(nt) that returns the reverse-complement of a DNA sequence.

def anti(seq):
    rev = seq[::-1]
    rc = ''
    for nt in rev:
        if nt == 'A': rc += 'T'
        if nt == 'C': rc += 'G'
        if nt == 'G': rc += 'C'
        if nt == 'T': rc += 'A'
    return rc

def shotgun_sim(seq,n, k):
    subs = []
    for _ in range(n):
        x = random.randint(0, len(seq)-k)
        subseq = seq[x:x+k]
        if random.random() < 0.5: subseq = anti(subseq)
        subs.append(subseq)

    return subs


import random
import sys

def mutate(s, p):
    seq = list(s)
    for i in range(len(seq)):
        if random.random() < p:
            if seq[i] == 'A': seq[i] = random.choice('CGT')
            elif seq[i] == 'C': seq[i] = random.choice('AGT')
            elif seq[i] == 'G': seq[i] = random.choice('ACT')
            elif seq[i] == 'T': seq[i] = random.choice('ACG')
    return ''.join(seq)


dna = 'AAAAAAAAAAAAAAAAAA'
dna = mutate(dna, 0.3)
print(dna)

# random dna
import random
import sys
import math 

def random_dna(n, X=[0.25, 0.25, 0.25, 0.25]): # default probability distribution
    if not math.isclose(1.0, sum(X)): sys.exit('oops') # if X doesn't add to 1
    a = X[0]
    c = X[0] + X[1]
    g = X[0] + X[1] + X[2]
    rseq =''
    for _ in range(n):
        r = random.random()
        if r < a: rseq += 'A'
        elif r < c: rseq += 'C'
        elif r < g: rseq += 'G'
        else: rseq +='T'
    return rseq

for i in range(5):
    print(i, random_dna(10, X =[0.1, 0.7, 0.1, 0.8])) # X = [A, C, G, T], probabilities, need to add 1
