# Кортежи в pattern matching

def print_data(user):
    match user:
        case ("Tom", 37):
            print("default user")
        case ("Tom", age):
            print(f"Age: {age}")
        case (name, 22):
            print(f"Name: {name}")
        case (name, age):
            print(f"Name: {name}  Age: {age}")
 
 
print_data(("Tom", 37))     # default user
print_data(("Tom", 28))     # Age: 28
print_data(("Sam", 22))     # Name: Sam
print_data(("Bob", 41))     # Name: Bob  Age: 41
print_data(("Tom", 33, "Google"))    # не соответствует ни одному из шаблонов

# Альтернативные значения
def print_data(user):
    match user:
        case ("Tom" | "Tomas" | "Tommy", 37):
            print("default user")
        case ("Tom", age):
            print(f"Age: {age}")
        case (name, 22):
            print(f"Name: {name}")
        case (name, age):
            print(f"Name: {name}  Age: {age}")
 
 
print_data(("Tom", 37))     # default user
print_data(("Tomas", 37))   # default user
print_data(("Tom", 28))     # Age: 28
print_data(("Sam", 37))     # Name: Sam  Age: 37

# Aльтернативные кортежи
def print_data(user):
    match user:
        case ("Tom", 37) | ("Sam", 22):
            print("default user")
        case (name, age):
            print(f"Name: {name}  Age: {age}")
 
 
print_data(("Tom", 37))     # default user
print_data(("Sam", 22))     # default user
print_data(("Mike", 28))    # Name: Mike  Age: 28

# Пропуск элементов
def print_data(user):
    match user:
        case ("Tom", 37):
            print("default user")
        case (name, _):     # второй элемент не важен
            print(f"Name: {name}")
 
 
print_data(("Tom", 37))     # default user
print_data(("Sam", 25))     # Name: Sam
print_data(("Bob", 41))     # Name: Bob

# Kортежей с разным количеством элементов
def print_data(user):
    match user:
        case (name, age):
            print(f"Name: {name}  Age: {age}")
        case (name, age, company):
            print(f"Name: {name}  Age: {age}  Company: {company}")
        case (name, age, company, lang):
            print(f"Name: {name}  Age: {age}  Company: {company} Language: {lang}")
 
 
print_data(("Tom", 37))                     # Name: Tom  Age: 37
print_data(("Sam", 22, "Microsoft"))        # Name: Sam  Age: 22  Company: Microsoft
print_data(("Bob", 41, "Google", "english"))    
# Name: Bob  Age: 41  Company: Google Language: english

# Кортеж с неопределенным количеством элементов
def print_data(user):
    match user:
        case ("Tom", 37, *rest):
            print(f"Rest: {rest}")
        case (name, age, *rest):
            print(f"{name} ({age}): {rest}")
 
 
print_data(("Tom", 37))               # Rest: []
print_data(("Tom", 37, "Google"))     # Rest: ["Google"]
print_data(("Bob", 41, "Microsoft", "english"))     # Bob (41): ["Microsoft", "english"]

# Если нам этот параметр (rest) не важен, но мы по прежнему хотим, чтобы шаблон соответствовал кортежу
# с неопределенным количеством элементов, мы можем использовать подшаблон *_:
def print_data(user):
    match user:
        case ("Tom", 37, *_):
            print("Default user")
        case (name, age, *_):
            print(f"{name} ({age})")
 
 
print_data(("Tom", 37))               # Default user
print_data(("Tom", 37, "Google"))     # Default user
print_data(("Bob", 41, "Microsoft", "english"))     # Bob (41)

# Также в match можно использовать словари и массивы