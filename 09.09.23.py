'''
Классы:

class название_класса:
    атрибуты класса
    методы класса

объект.метод([параметры метода])
'''

# Пример1
# class Person:

#     def say(self, message):
#         print(message)

#     def say_hello(self):
#         self.say('Hello python')

# tom = Person()
# bob = Person()

# tom.say_hello()
# bob.say_hello()

# tom.say('Привет')

# Пример 2

# class Person:
#     # конструктор
#     def __init__(self):
#         print('Создание объекта Person')

#     def say_hello(self):
#         print('Hello python')

# tom = Person() # Создание объекта Person
# tom.say_hello()


# class Person:
#     # конструктор
#     def __init__(self, name):
#         self.name = name # имя человека
#         self.age = 1 # возраст человека
        

#     def say_hello(self):
#         print('Hello python')

# tom = Person('Tom')
# bob = Person('Bob')

# print(f'name: {tom.name}')
# print(f'age: {tom.age}')

# tom.age = 20
# print(f'age: {tom.age}')


# class Person:
#     # конструктор
#     def __init__(self, name, age):
#         self.name = name # имя человека
#         self.age = age # возраст человека
        

#     def display_info(self):
#         print(f'Name: {self.name} Age: {self.age}')

# tom = Person("Tom", 20)
# bob = Person('Bob', 25)

# tom.display_info()
# bob.display_info()