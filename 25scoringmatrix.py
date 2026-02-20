# Write a program that can print out a match-mismatch scoring matrix. 
import sys 

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

# header
print('  ', end='')
for c in alph: print(c, end='  ')
print()

for i in range(len(alph)):
    print(alph[i], end=' ')
    for j in range(len(alph)):
        if i == j: print(mat, end=' ')
        else: print(mis, end=' ')
    print('')