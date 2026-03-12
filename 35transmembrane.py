
import sys 

aas = 'ACDEFGHIKLMNPQRSTVWY'
kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
    -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)

def hydropathy(pro):
    total = 0
    for aa in pro:
        idx = aas.find(aa)
        if idx != -1:
            total += kdh[idx]
    return total / len(pro)

def has_signal_pep(seq):
    for i in range(0, 30 - 8 +1):
        window = seq[i:i+8]
        if 'P' not in window and hydropathy(window) >= 2.5:
            return True
        return False

def has_tm_region(seq):
    for i in range(30, len(seq) - 11 +1):
        window = seq[i:i+11]
        if 'P' not in window and hydropathy(window) >= 2.0:
            return True
        return False 

for defline, seq in read_fasta(sys.argv[1]):
    if has_signal_pep(seq) and has_tm_region(seq):
        print(defline[:60])


