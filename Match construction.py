"""
Конструкция match

Pattern matching представляет применение конструкции match, которая позволяет 
сопоставить выражение с некоторым шаблоном.
Если выражение соответствует шаблону, то выполняются определенные действия. 
В этом смысле конструкция match похожа на конструкцию if/else/elif.
Функциональность match гораздо шире - она также позволяет извлечь данные из составных 
типов и применить действия к различным частям объектов.
"""
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("hello")
        case "german":
            print("hallo")
        case _:                 # действия по умолчанию, если нет совпадения
            print("undefined")

print_hello("english")
print_hello("german")
print_hello("russian")
print_hello("spanish")

"""
Также можно определить блок case, который позволяет сравнивать сразу с несколькими знечениями. 
В этом случае значения разделяются вертикальной чертой
"""
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "american english" | "british english" | "english":
            print("Hello")
        case _:
            print("Undefined")
 
 
print_hello("english")              # Hello
print_hello("american english")     # Hello
print_hello("spanish")              # Undefined

# Можно сравнивать выражения с данными других типов
def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0
 
 
print(operation(10, 5, 1))      # 15
print(operation(10, 5, 2))      # 5
print(operation(10, 5, 3))      # 50
print(operation(10, 5, 4))      # 0