# 12phred.py by Iris Moore
# Write functions that convert quality value symbols into error rates and vice-versa. 
# The ord() function returns the ASCII value of a letter. 
# The chr() function turns an ASCII value into a letter.

# quality score Q = -10 * log10(p) 
# Q = ord(letter) - 33
# 'A' = 65, Q= 65 - 33 = 32 
# Q + 33 = ASCII

def char_to_prob(c):
    if len(c) != 1: return None 
    q = ord(c) - 33
    if q < 0 or q > 93: return None 
    return 10 ** (-q / 10)
print(char_to_prob('A'))

import math

def prob_to_char(p):
    if p <= 0 or p >= 1: return None
    score = -10 * math.log10(p)
    q = round(score)
    if q < 0 or q > 93: return None 
    return chr(q + 33)
print(prob_to_char(0.001))
