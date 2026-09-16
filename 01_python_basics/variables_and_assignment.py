x=5
y=10

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
