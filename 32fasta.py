import mcb185
import sys

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline[:30], seq[:40], len(seq))

# run with python3 32fasta.py ../MCB185/data/(fa.gz file)