
data = 'apple,banana,orange'
print(data.split(','))

text = 'Python123'
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())

text = 'Python Prgramming'
vowels = 'aeiou'
count = 0
for ch in text.lower():
    if ch in vowels:
        count += 1
print(f'Vowe count: {count}')

# Task 1. Reverse a string
text = input('Enter a string: ')
reversed_text = text[::-1]
print(f'Reversed string: {reversed_text}')
print()

# Task 2. Count words in a sentence
sentence = input('Enter a sentence: ')
words = sentence.split()
print(f'Word count: {len(words)}')
print()

# Task 3. Check palindrome
text = input('Enter a word: ')
if text == text[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')
print()

# Task 4. Count frequency of each character
text = input('Enter a string: ')
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print('Character frequency', freq)
print()

# Task 5. Capitalize first lette of each word
sentence = input('Enter a sentence: ')
result = sentence.title()
print('Capitalized: ', result)
