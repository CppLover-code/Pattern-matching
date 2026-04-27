# Классы в pattern matching
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def print_person(person):
    match person:
        # Каждый шаблон представляет собой определение Person, 
        # где с каждым атрибутом сопоставляется некоторое значение. 
        case Person(name="Tom", age=37):
            print("Default Person")
        case Person(name=name, age=37):
            print(f"Name: {name}")
        case Person(name="Tom", age=age):
            print(f"Age: {age}")
        case Person(name=name, age=age):
            print(f"Name: {name}  Age: {age}")
 
# Стоит отметить, что этот шаблон - это НЕ вызов конструктора Person. 
# Шаблон просто устанавливает, как атрибуты сопоставляются со значениями.
 
print_person(Person("Tom", 37))  # Default person
print_person(Person("Tom", 22))  # Age: 22
print_person(Person("Sam", 37))  # Name: Sam
print_person(Person("Bob", 41))  # Name: Bob  Age: 41

# Передача набора значений
def print_person(person):
    match person:
        case Person(name="Tom" | "Tomas" | "Tommy"):
            print("Default Person")
        case Person(name=person_name):         # получаем только атрибут name
            print(f"Name: {person_name}")
        case _:
            print("Not a Person")
 
 
print_person(Person("Tom", 37))     # Default person
print_person(Person("Tomas", 37))   # Default person

# альтернативные значения
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
class Student:
    def __init__(self, name):
        self.name = name
 
 
def print_person(person):
    match person:
        case Person(name="Tom") | Student(name="Tomas"):
            print("Default Person/Student")
        case Person(name=name) | Student(name=name):    # получаем только атрибут name
            print(f"Name: {name}")
        case _:
            print("Not a Person or Student")
 
 
print_person(Person("Tom", 37))     # Default Person/Student
print_person(Student("Tomas"))      # Default Person/Student
 
 
print_person(Person("Bob", 41))     # Name: Bob
print_person(Student("Mike"))       # Name: Mike
 
print_person("Tom")                 # Not a Person or Student