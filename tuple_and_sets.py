# Tuples
marks = (70, 85, 90, 75, 60)
names = ('Amit', 'Deepseek', 'Ravi')
single = (10,)

print('Min:', min(marks))
print('Max:', max(marks))

print()

# Accessing names
for name in names:
    print(name)

# Access Tuple items
print(marks[0])
print(marks[-1])

print()

# Loop through a tuple
for m in marks:
    print(m)

print()

# Tuple unpacking
a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)

# Sets
numbers = {10, 20, 30, 40}
duplicates = {1, 2, 2, 2, 3, 3}
print(duplicates)

# Add and Remove Items
numbers.add(50)
numbers.remove(40)
numbers.discard(100)
print(numbers)

# Loop through a set
for n in numbers:
    print(n)

print()

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print('Union:', a|b)
print('Intersection:', a&b)
print('Difference:', a-b)

# Unique Visitors
visitors = ['A', 'B', 'A', 'C', 'B', 'D']
unique_visitors = set(visitors)
print('Total unique visitors:', unique_visitors)

print()
# Qtn1: Convert list with duplicates to unique values
numbers = [1, 1, 2, 2, 3, 1, 5, 2, 6, 4 ,4, 2, 4]
unique_values = set(numbers)
print(unique_values)

print()

# # Qtn2: Check if value exists in a set
# numbers = {1, 2, 3, 4, 5, 2}
# value = int(input('Enter a value to check: '))

# if value in numbers:
#     print('Value exists')
# else:
#     print('Value does not exist')

print()

# Qtn3: Find common elements between two lists
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print(set(lst1) & set(lst2))

print()

# Qtn4: Use tupls to store date and print nicely
date = (22, 'January', 2026)
day, month, year = date
print('Date:', day, month, year)

print()

# Qtn5: Swap two variables using tuple
a = 10
b = 20
a, b = b, a
print('a:', a)
print('b', b)


print('\n---statistics---')
a = {1, 2, 3}
b = {3, 4, 5}

print(a & b) # Intersection
print(a | b) # Union
print(a - b) # whats found in a but not in b
print(b - a) # whats found in b but not in a
print(a ^ b)
