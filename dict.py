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

# Delete items
del student['age']
print(student)

student.pop('marks')
print(student)
