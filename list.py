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


# Task 1: Create a list of 5 numbers and print sum
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num

print('Sum:',total)

# Task 2: Find maximum value in list
numbers = [12, 45, 7, 89, 34, 67, 99]
max_value = numbers[0]
for n in numbers:
    if n > max_value:
        max_value = n

print('Max Value:', max_value)

# Task 3: Count how many marks are above 75
marks = [70, 85, 60, 90, 75, 88]
count = 0
for m in marks:
    if m > 75:
        count += 1

print('Marks above 75:', count)

# Task 4: Replace lowest mark with 0
marks = [70, 85, 60, 90, 75]
min_marks = marks[0]
for m in marks:
    if m < min_marks:
        min_marks = m

index = marks.index(min_marks)
marks[index] = 0

print('Updated marks:', marks)

# Task 5: Reverse a list using loop
numbers = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print('Reversed list:', reversed_list)
