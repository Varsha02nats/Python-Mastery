from pyparsing import nums
from sympy import python


x=5
y=10

z= x+y
print(z) # Output: 15
a,b = 6,9
a,b = b,a

#i=j=0

count=0
count+=1

#star - unpacking
first, *middle, last = [1,2,3,4,5]
print(first)  # Output: 1
print(middle) # Output: [2, 3, 4]
print(last)   # Output: 5

first, *last = [1,2,3,4,5]
print(first)  # Output: 1
print(last)   # Output: [2, 3, 4, 5]

first, *middle, last = [1,2]
print(first)  # Output: 1
print(middle) # Output: []
print(last)   # Output: 2

#infinity
best_score = float('inf') #+infinity(start value for a running minimum)
worst_score = float('-inf') #-infinity(start value for a running maximum)

for _ in range(3):    #_ = "I don't care about this variable"
    pass


#How to swap two variables without using a temporary variable
#You can swap two variables in Python without using a temporary variable by using tuple unpacking. Here's an example:
#```python
#a = 5
#b = 10
#a, b = b, a
#print(a)  # Output: 10
#print(b)  # Output: 5
#```


p, q = 1, 2 

for _ in range(3):
    p, q = q, p+q    #right side uses old values of p and q to compute new values, then assigns them to p and q simultaneously
print("The value of p is:", p)  # Output: 5
print("The value of q is:", q)  # Output: 8


def classify_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(classify_number(10))   # Output: Positive
print(classify_number(-5))   # Output: Negative
print(classify_number(0))    # Output: Zero


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence