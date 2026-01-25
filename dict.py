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


print('\n---Practice tasks---\n')
# Create a dictionary with 5 products with prices
# Find total price of all products
# Find product with highest price
# Update price of one product
# Remove a product


# Task 1. Create a dictionary of 5 products with prices
products = {
    'Laptop': 55000,
    'Mouse': 500,
    'Keyboard': 1200,
    'Monitor': 15000,
    'Headphones': 2500,
    'Table': 200000,
    'Mat': 500
}
print(products)

print()

# Task 2. Find the total price of all products
total = 0
for m in products.values():
    total = total + m
print(f'Total price ${total}')

print()

# Task 3. Find product with highest price
highest_product = None
highest_price = 0
for product, price in products.items():
    if price > highest_price:
        highest_price = price
        highest_product = product
print(f'Highest price product {highest_product}')
print(f'Price ${highest_price}')

print()

# Task 4. Update price of one product
products['Mouse'] = 650
print(f'Updated products: {products}')

print()

# Task 5. Remove a product
products.pop('Keyboard')
print(f'After removal: {products}')


