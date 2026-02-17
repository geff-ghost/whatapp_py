# Practice Tasks

# 1. Fuction to calculate square of a number
def square(n):
    return n*n

# print(square(5))

# 2. Fuction to check prime number
def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# print(is_prime(7))
# print(is_prime(10))

# 3. Function to find maximum of two numbers
def find_max(a, b):
    if a > b:
        return a
    return b

# print(find_max(10, 20))

# 4. Fuction to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal*rate*time)/100

# print(simple_interest(1000, 5, 2))

# 5. Function to count vowels in a string
def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# print(count_vowels('Python Programming'))

def add(a,b):
    print(a + b)

result = add(2, 3)
print(result)

def func(x):
    x += 10

a = 5
func(a)
print


