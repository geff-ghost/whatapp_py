
# Opening a file
# Basic syntax: file = open("data.txt", "r")
# 'r': read, 'w': write(overwrite): 'a': append, 'r+': read and write

# Reading entire file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

print("-----------")

# Read line by line
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()

print("-----------")

# Read one line:
file = open("data.txt", "r")
print(file.readline(6))
file.close()

# Write mode (overwrites file):
file = open("output.txt", "w")
file.write("Hello Python\n")
file.write("File handling is very easy.")
file.close()

# Append mode (adds at end):
file = open("output.txt", "a")
file.write("\nNew line added")
file.close()

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

print("-----------")

# Create a file and write 5 names
with open ("names.txt", "w") as file:
    file.write("Amit\n")
    file.write("Deepak\n")
    file.write("Ravin\n")
    file.write("Neha\n")
    file.write("Kiran\n")

# Read file and print each line
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())

# Append new data to file
with open("names.txt", "a") as file:
    file.write("Suman\n")
    file.write("Rahul\n")

with open("names.txt", "r") as file:
    print(file.readlines())
    content = file.read()
    print(content)

print("-----------")

# Read marks from file and calculate average
total = 0
count = 0
with open("marks.txt", "r") as file:
    for line in file:
        name, marks = line.split()
        total += int(marks)
        count += 1
average = total / count
print("Average marks:", average)

