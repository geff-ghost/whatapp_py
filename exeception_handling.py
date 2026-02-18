
# Handling specific errors 
# ZeroDivisionError
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# ValueError
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")

# Multiple exceptions
try:
    # num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Enter valid number.")

# Exception as variable (see real error)
try:
    print(10 / 0)
except Exception as e:
    print(f"Error: {e}")

# finally block (Always runs)
'Runs whether error occurs or not.'
try:
    print("Opening file")
except:
    print("Error occured")
finally:
    print("Program finished")

# else block (runs if no error)
try:
    num = int(input("Enter number: "))
except:
    print("Invalid input")
else:
    print(f"You entered {num}")

# Open file safely with error handling
try:
    with open("me.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File does not exist")

# Safe list index access
numbers = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    print(numbers[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Enter valid index number")
