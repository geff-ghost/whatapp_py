import csv

# Reading CSV file
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


print("\n")
# Skip Header Row
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #skip header
    next(reader) # skips the next line
    for row in reader:
        print(row)


print("\n")
# Access Individual Columns
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for i, row in enumerate(reader):
        name = row[0]
        marks = row[1]
        print(f"{i} {name}: {marks}")
    
# Writing to CSV file
data = [
    ["Name", "Marks"],
    ["Amit", 78],
    ["Deepak", 85]
]
with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)


print("\n")
# Calculate Average Marks from CSV
total = 0
count = 0
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        total += int(row[1])
        count += 1
    average = total / count
    print("Average marks:", average)

print("\n")
# CSV Dictionary Reader
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Marks"])

print("\n")
# Practice tasks
print("Practice task begins from here")
# Read CSV and print only student names
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row["Name"]}")

print("\n")
# Count students who scored above 80
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["Marks"]) > 80:
            count += 1
    print("Students scoring above 80:", count)

print("\n")
# Find highest scorer from CSV
highest_marks = -1
topper = ""
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks = int(row["Marks"])
        if marks > highest_marks:
            highest_marks = marks
            topper = row["Name"]
    print("Topper:", topper)
    print("Highest Marks:", highest_marks)

print("\n")
# Convert CSV data into dictionary
students = {}
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students[row["Name"]] = int(row["Marks"])

print(students)

