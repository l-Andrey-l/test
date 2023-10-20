# Пример 1
# class Person:
#     type = 'Person'
#     description = 'Desc a person'


# print(Person.type)
# print(Person.description)

# Person.type = 'Class Person'
# print(Person.type)

# Пример 2

# class Person:
#     type = 'Person'

#     def __init__(self, name):
#         self.name = name


# tom = Person('Tom')
# bob = Person('Bob')

# print(tom.type)
# print(bob.type)

# Person.type = 'Class Person'

# print(tom.type)
# print(bob.type)

# Пример 3

# class Person:
#     default_name = 'Undefined'

#     def __init__(self, name):
#         if name: self.name = name
#         else: self.name = Person.default_name


# tom = Person('')
# bob = Person('Bob')

# print(tom.name)
# print(bob.name)


# Пример 4

# class Person:
#     name = 'Undefined'

#     def print_name(self):
#         print(self.name)

# tom = Person()
# bob = Person()

# tom.print_name()
# bob.print_name()

# bob.name = 'Bob'
# tom.print_name()
# bob.print_name()

# Person.name = 'some Person'
# tom.print_name()
# bob.print_name()

# Cтатические методы

# class Person:

#     __type = 'Person'

#     @staticmethod
#     def print_type():
#         print(Person.__type)


# Person.print_type()

# tom = Person()
# tom.print_type()