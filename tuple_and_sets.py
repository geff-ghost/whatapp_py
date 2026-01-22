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


