# Write a function that returns the minimum and maximum value of a list.
# can't use print(min(values))
def minimum(values):
    my_min = values[0] #start at first value
    my_max = values[0]
    for value in values:
        if value < my_min: my_min = value
        if value > my_max: my_max = value
    return my_min, my_max 

x = [3.14, 2.719, 1/7, 0, -2, 1]
for i, v in enumerate(x): # enumerate returns tuple
    print(i, v)

# Write a function that returns the mean of the values in a list.
def mean(values):
    total = 0
    for value in values:
        total = total + value
    return total / len(values)

x = [0.1, -3, 39, 4.5]
print(mean(x))

# Write a function that computes the entropy of a probability distribution.
import math 

def mysum(values):
    total = 0
    for value in values: total += value
    return total
def entropy(P):
    if not math.isclose(mysum(P), 1.0): sys.exit('nooo')
    H = 0
    for p in P:
        H -= p * math.log2(p)
    return H

x = [0.25, 0.25, 0.25, 0.25]
print(entropy(x))

# Write a function that computes the Kullback-Leibler distance between two sets of probability distributions.


def dkl(P, Q):
    if not math.isclose(mysum(P), 1.0): sys.exit('noooo')
    if not math.isclose(mysum(Q), 1.0): sys.exit()
    d = 0
    for p, q in zip(P, Q):
        d += p * math.log2(p/q)
    return d

x = [0.1, 0.2, 0.3, 0.4]
y = [0.4, 0.3, 0.2, 0.1]
print(dkl(x, y))