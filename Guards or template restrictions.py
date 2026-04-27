"""
Guard или ограничения шаблонов позволяют установить дополнительные условия, 
которым должно соответсвовать выражение. Ограничение задается сразу после шаблона 
с помощью ключевого слова if, после которого идет условие ограничения
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, доступ запрещен")
        case Person(name=name):
            print(f"{name}, добро пожаловать!")
 
 
enter(Person("Tom", 37))        # Tom, добро пожаловать!
enter(Person("Sam", 12))        # Sam, доступ запрещен

# **********************************************************************************
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, доступ запрещен")
        case Person(name=name, age=age) if age < 22:
            print(f"{name}, доступ  ограничен")
        case Person(name=name):
            print(f"{name}, у вас полноценный доступ!")
 
 
enter(Person("Tom", 37))        # Tom, у вас полноценный доступ!
enter(Person("Bob", 20))        # Bob, доступ  ограничен
enter(Person("Sam", 12))        # Sam, доступ запрещен

# **********************************************************************************
def check_data(data):
    match data:
        case name, age if name == "admin" or age not in range(1, 101):
            print("Некорректные значения")
        case name, age:
            print(f"Данные проверены. Name: {name}  Age: {age}")
 
 
check_data(("admin", -45))      # Некорректные значения
check_data(("Tom", 37))         # Данные проверены. Name: Tom  Age: 37