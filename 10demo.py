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

import math

def circle_area(r): return (math.pi) * r ** 2
def rectangle_area(w, h): return w * h 
def triangle_area(w, h): return rectangle_area(w, h)/2

# Compute the arithmetic mean of 3 numbers
def arithmean(n1, n2, n3): 
    return ((n1+n2+n3)/3)
print(arithmean(1, 2, 3))

# Convert temperature from F to C or vice-versa
def ftoc(f): 
    return ((f - 32)*5/9) 
print(ftoc(32))

def ctof(c):
    return ((c* 9/5)+ 32)
print(ctof(0))

a = 2
b = 2
if a == b: 
    print('a equals b')
    print(a, b) # only prints if condition true
print (a, b) # always prints 

def is_even(x):
    if x % 2 == 0: return True 
    return False 
print(is_even(2))
print(is_even(3))

c = a == b # a == b is boolean expression because it's true or false
print(c) 
print(type(c))

a = 1
b = 2
if a < b: 
    print('a < b')
elif a > b: 
    print('a > b')
else: 
    print('a == b') # use == unless assigning variable
# in if-elif-else construct only the first true conditions is executed

# floating point numbers have finite precision so this code gives a < b. Never test for equality b/w them.

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else: print('a == b')

# Instead examine their difference. They're close enough if the difference is less than some acceptable value.

a = 0.3
b = 0.1 * 3
print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

# Compare two values with math.isclose()

a = 0.3
b = 0.1 * 3
if math.isclose(a, b): print('close enough')

# strings are compared by ASCII values. Variables need to be the same type or there's type error 
# ex: s1= 'A' s2 = 3

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('A < a')

# None type: if you call (print) a function without returning (running) it, you won't get a value.
# ex: def silly(m, x, b): y = m * x + b
# print(silly(2, 3 ,4)) ---> value= None


def is_integer(x):
    if x % 1 == 0: return True
    return False
print(is_integer(2))

# Write a function that returns the complement of a DNA letter, returning None if the letter isn't DNA.

def dnacomp(x):
    if x == 'A': return 'T'
    elif x == 'T': return 'A'
    elif x == 'C': return 'G'
    elif x == 'G': return 'C'
    else: return None
print(dnacomp('A'))

# Write a function that returns the maximum of 3 numbers. 
# To be clear, the function takes 3 input parameters and returns the single largest one.

def maxnum(x, y, z):
    if x > y and x > z: return x 
    elif y > x and y > z: return y
    else: return z
print(maxnum(1, 2, 3))

# While loop: while (Boolean is True): do_something

# while True: 
    # print('hello')
# ctrl c stops loop 
# break= break loop at certain point

i = 0 
while True:
    i = i + 1
    print('hey', i) # gives hey 1, hey 2
    if i == 3: break 

i = 0 # i starts at 0, can start at 1, 2 etc
while i < 3: # condition for when it's no longer True/ when to stop
    i = i + 1 # go by 1, can do i + 2, skip by 2s
    print('hey', i) 

# for i in range (for loop) 

for i in range(1, 10, 3): 
    print(i)
# range(initial value, end before, increment) but usually they increment by 1

for i in range (0, 5): # same as for i in range(5) 
    print(i)

for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else: print(i, 'is odd')

