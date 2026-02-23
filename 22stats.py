# Write a program that reports descriptive stats for numbers on the command line. Your program should report the following values:
# The number of values, minimum and maximum values
# The mean and standard deviation, median value
import sys
numbers = [float(x) for x in sys.argv[1:]] 
count = len(numbers)
minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers)/count 

# stdev = 0 
variance = 0
for x in numbers:
    variance += (x - mean)**2 
variance /= count 
stdev = variance **0.5
numbers.sort()
if count % 2 == 0:
    median = numbers[count // 2 ] # divide but only take integer 
else: 
    mid1 = numbers[count // 2 - 1]
    mid2 = numbers[count // 2]
    median = (mid1 + mid2)/2

print('Count:', count)
print('Minimum:', minimum)
print('Maximum:', maximum)
print('Mean:', mean)
print('Standard Deviation:', stdev)
print('Median', median)