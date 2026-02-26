# Encapsulation = protecting data inside a class

# Public Variables
class Student:
    def __init__(self):
        self.name = 'Deepak'

s = Student()
print(s.name)

# Protected Variables (_variable)
class Student:
    def __init__(self):
        self._marks = 85

s = Student()
print(s._marks)

# Private Variables (__variable)
class Student:
    def __init__(self):
        self.__marks = 90
    
    def get_marks(self):
        return self.__marks

s = Student()
print(s.get_marks())
