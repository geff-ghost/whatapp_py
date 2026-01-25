student = {
    'name': 'Deepak',
    'age': 25,
    'marks': 85
}
print(student['name'])
print(student['age'])

# Safe access
print(student.get('marks'))
print(student.get('grade', 'Not found'))

# Adding a new key
student['grade'] = 'A'

print(student)

# Update a value
student['marks'] = 89
print(student)

# loop through a dict
# keys only
for key in student.keys():
    print(key)

print()
# values only
for value in student.values():
    print(value)

print()
# keys and values
for key, value in student.items():
    print(key, ':', value)

print()
# check existance
if 'number' in student:
    print('Key exists')

print()
# real example. Student marks record
marks = {
    'Math': 85, 
    'Science': 90,
    'English': 78
}
total = 0
for m in marks.values():
    total = total + m
average = total / len(marks)
print(f'Total: {total}')
print(f'Average: {average:.2f}')

