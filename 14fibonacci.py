# 14fibonacci.py by Iris Moore
#  reports the first 10 numbers from the Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

a = 0
b = 1 # first two fib numbers 
for i in range(10): # up to 10
    print(a) # print current fib number
    a, b = b, a + b

 
# for first 100

a = 0
b = 1
for i in range(100):
    print(a)
    a, b = b, a + b 