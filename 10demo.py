# 10demo.py by Iris Moore

print ('hello, again') # greeting

print(1.5e-2)

print(2**3) # 2**3= 2^3 

print(5//2) # integer division= ignores remainder 

print(5%2) # gives only remainder

print(pow(2,3)) # x to the power of y

import math

print(math.e)
print(math.factorial(10))

# Write function is_prob(x) that determines boolean if a number is a valid probability x>=0, x<=1 

def is_prob(x):
    return x>=0 and x<=1
print(is_prob(0.5)) 

# Write function distance(x1, y1, x2, y2) that computes cartesian distance between two points on a graph 

# def (distance(x1, y1, x2, y2))
   #return math.sqrt((x2 -x1)**2 + (y2 -y1)**2)
# print(distance())

# 19) fibonacci, print out first 100 numbers of fibonacci seq
# 1 1 2 3 5 8 13 21

a=1
b=1
fib = a + b 
print(fib)

while True:
    a = b
    b = fib
    fib= a + b 
    print(fib)
    if fib > 100: break

# a = 5 b = 3, how can you swap the variables? need additional variable to swap
# a = ...
# b = ...
# c = a 
# a = 

def min4(a, b, c, d ): 
    if a <= b and a <= c and a <= d: return a 
    if b <= c and b <= d: return b # stepwise, use less than for all
    if c <= d: return c 
    return d 

print (min4(5, 3, -1, 0)) 

def pythagoras(a, b): 
    return (a**2 + b**2)**0.5 
print(pythagoras(3, 4))
