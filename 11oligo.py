# 11oligo.py by Iris Moore
# Write a function that returns the oligo melting temperature given the number of As, Cs, Gs, and Ts in the oligo. 
# Use these two methods.

# For oligos <= 13 nt, Tm = (A+T)*2 + (G+C)*4 
# For longer oligos, Tm = 64.9 + 41*(G+C -16.4) / (A+T+G+C)

def tm(A, T, C, G):
    total = (A + T + C + G) # make variable for adding number of nts
    if total <= 13: return (A + T) * 2 + (G + C) * 4
    else: return 64.9 + 41 * (G + C - 16.4) / (A + T + C + G)
print(tm(5, 7, 3, 4))
