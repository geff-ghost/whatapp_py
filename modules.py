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

