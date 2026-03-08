import sys

def read_fasta(filename):
    seq = []
    with open(filename) as fp:
        for line in fp:
            seq.append(line.rstrip())
    seqline = ''.join(seq[1:]) # glue together sequences
    words = seq[0]
    uid = words.split()[0][1:]
    return uid, seqline

uid, seq = read_fasta(sys.argv[1])
print(uid, seq)


import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline, seq)
    for frame in range(3):
        pro = mcb185.translate(seq(frame))
        print(' ', pro)

import random
import sys 

def random_words_list(n, k):
    words = []
words1 = random_word_list(size,5)
words2 = random_word_list(size,5)

for word in words1:
    if word in words2:
        found += 1
        print('hooray, found:', word)

# opening files
with open(path) as fp:
    for line in fp:
        do_something_with(line)

# compressed files
import gzip
with gzip.open(path, 'rt') as fp:
    for line in fp:
        print(line, end='')

        