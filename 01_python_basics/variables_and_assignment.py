from sympy import python


x=5
y=10

z= x+y
print(z) # Output: 15
a,b = 6,9
a,b = b,a

i=j=0

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

#Simulataneous assignment allows you to assign values to multiple variables in a single line. This can be useful for swapping values or initializing multiple variables at once.

#Simulataneous assignment evaluates the whole right-hand side of the assignment before performing the assignments. This means that the values are computed first, and then assigned to the variables in the order they appear on the left-hand side.

p, q = 1, 2 

#for example, in the line `p, q = 1, 2`, the values `1` and `2` are evaluated first, and then assigned to `p` and `q` respectively. This allows for a concise and efficient way to assign multiple variables at once.

for _ in range(3):
    p, q = q, p+q    #right side uses old values of p and q to compute new values, then assigns them to p and q simultaneously
print("The value of p is:", p)  # Output: 5
print("The value of q is:", q)  # Output: 8