
numbers = [10, 20, 30, 40]

# Access list items
print(numbers[0])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])

# Update list items
numbers[1] = 25
print(numbers)

# Add items to list
numbers.append(50) # add at the end
numbers.insert(3, 77) # adds at specific index
print(numbers)
# Remove items
numbers.remove(30) # remove by value
numbers.pop(0) # remove by index
print(numbers)
numbers.clear() # clear the list

# List length
numbers = [10, 20, 30]
print(len(numbers))

# Loop through a list
marks = [70, 85, 60, 90, 75]
for m in marks:
    print(m)
# Loop with index
for i in range(len(numbers)):
    print(i, marks[i])

# Real example: Student marks analysis
marks = [70, 85, 60, 90, 75]
total = 0
for m in marks:
    total = total + m
average = total / len(marks)
print('Total:', total)
print('Average:', average)
