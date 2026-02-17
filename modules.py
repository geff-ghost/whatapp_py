"""Types of modules
- Built-in modules
- User-defined modules
"""
# math module
import math
print(math.sqrt(25))
print(math.factorial(5))

# random module
import random
print(random.randint(1, 100))
print(random.choice([10, 20, 30]))

# datatime module
from datetime import datetime
now = datetime.now()
print(now)

# Import specific function
from math import sqrt
print(sqrt(16))

# Import with alias
import math as m
print(m.sqrt(144))


# Task 1. Import math and print cube root
import math
num = 27
cube_root = num **(1/3)
print(cube_root)
print(math.pow(27, 1/3))

# Task 2. Generate random password using random
import random
import string
characters = string.ascii_letters + string.digits
password = ''
for i in range(8):
    password += random.choice(characters)
print(password)

# Task 3. Print current date and time
from datetime import datetime
now = datetime.now()
print(now)


