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
    return d #no else: b/c outside function

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

# triangular number = sum of numbers from 1 to n

def triangular(n):
    tri = 0 # variable to hold sum, start at 0
    for i in range (n + 1):
        tri = tri + i
    return tri 
print(triangular(10))

# Write a function that calculates the factorial of a number.

def factorial(n):
    if n <= 0: return None # doesn't work if negative
    fact = 1 #variable holds function, start at 1
    for i in range(1, n + 1): 
        fact = fact * i 
    return fact 
print(factorial(2))

# Write a function to determine if a number is prime.

def is_prime(n):
    if n <= 1: return False
    for i in range (2, n): 
        if n % i == 0: return False 
    return True 
print(is_prime(4433))

def pythagoras (a, b):
    return (a ** 2 + b ** 2) ** 0.5
print(pythagoras(2, 3))

# Write a program ascii.py that prints out the ASCII decimal 
# values for A and a separated by a comma.

print(ord('A'), ord('a'), sep=',') # ord = print ASCII of letter

# Write a function is_prob(x) that determines (returns Boolean) 
# if a number is a valid probability (x >= 0 and x <= 1).

def is_prob(x):
    if x < 0 or x > 1: return False
    else: return True 
print(is_prob(1))

def is_int(x):
    if x % 1 == 0: return True 
    else: return False
print(is_int(2.1))

def mph_to_kph(x):
    return (x/0.62137)
print(mph_to_kph(24))

# Euler
import math 

n = 0 
e_estimate = 0
previous = -1

def distance(x1, y1, x2, y2):
    return ((x2- x1)**2 + (y2- y1)**2)**0.5
print(distance(0, 0, 3, 4))

# ascii.py
print(ord('A'), ord('a'), sep= ',')

# += means add to existing value x += 1: x = x + 1

# Write a program that finds all Pythagorean triples for triangles with 
# sides a and b less than 100. For example, 3, 4, 5 is a triple: 3^2 + 4^2 = 5^2. 
# Hint: all sides, including the hypotenuse, must be integers. 
# A good way to test for an integer is like: if c % 1 == 0.

for a in range (1, 100):
    for b in range (a, 100): # start at a avoid repeats
        c= (a**2 + b**2)**0.5 
        if c % 1 == 0: # if c is an integer, print the triple as an integer 0
            print(a, b, int(c))

s1 = 'hello'
s2 = 'world'
s3 = s1 + s2 
print(len(s3))
print(s3.count('o'), s3.count('l'))

s4 = s3.replace('o', 'i')
print(s4)

# s = 'blah blah'
# print(s[3]): h, start at zero

# s = 'blah blah'
# for c in s: 
#   print(c)

# s = 'blah blah'
# pos = 0
# for c in s:
#   if c == 'i': print('found i at pos', pos)
# pos += 1

# s = 'blah blah'
# for i in range(len(s)):
#   print(i, s[i])

#s = 'ABCDEF'
#.    012345
# print(s[0:4]) slice function , same as print(s[:4])

# for i in range (0, 4, 2):
#   print(i, s[i])
#print('first 4', s[:4])
#print('last 4', s[-4:]) before : beginning, after : end
# print(s[::-1]) reverses sequence

seq = 'CAGAGGATATATTCAGAGT'
print(seq)
for i in range(0, len(seq), 3):
    print(i, seq[i:i+3])

circle = (20, 50, 5)
print(circle[0]) # gives 2

# tuple:
basket = ('a', 50, 'cat', 3.14)
print(basket[::-1])
print(basket[0]) # a
print(basket[0:1]) # slice of unit that gives ('a',), slice of the basket

#lists
animals = ('cat', 'dog,', 'cow')
animals2 = list(animals) # gives in []
print(animals)
print(animals2)
basket = []
basket.append('apple')
basket.append('pear')
basket.append('peach')
basket.append('blueberry')
basket.sort() # sort alphabetical
basket.sort(reverse=True) #reverse order
print(basket)

seq = 'GATCACGAT' # can't sort string on own 
seq_list = list(seq) # turn into list
seq_list[3] = 'a' # replace C with a
seq_list.sort() # sort alphabetical
s = '-'.join(seq_list)

print(seq)
print(seq_list)
print(s)

a= ['cat', 'dog', 'rat']
b = a.copy() # copy of a 
b[0] = 'cow' # change to cow
print(b)
print(a)

# or can do a =[cat, cow]
# b=[] for animal in a: b.append(animal)

#split(): turn string to list
s = '3.14, 2.71, 1.51'
data = s.split(',') #split with commas
print(data)
pi = float(data[0]) #make floating point number
e = float(data[1])
v = pi + e #added 2 strings so doesn't add numbers correctly unless u float()
print(v)

s = 'ACGATAGATCGAG'
if 'AC' in s: print('yes, found AC')

# index- find position
s = 'ACGATAGATCGAG'
if 'A' in s: print('yes, found A')
if 'Y' in s:
    x = s.find('Y') # s.find() s.index() both fibnd position 
    print('Y found at position',x)
x = s.index('A')
print('A found at position', x)

animals = ['cat', 'dog', 'cow', 'pig']
if 'cow' in animals:
    x = animals.index('cow')
    print(x)