# Пример 1
# class Person:

#     def __init__(self, name):
#         self.name = name
#         self.age = 1

#     def display_info(self):
#         print(f'Имя: {self.name} \t Возраст: {self.age}')

# tom = Person('Tom')
# tom.display_info()
# print(tom.age)
# print(tom.name)
# tom.name = 'Bob'
# tom.age = 30
# tom.display_info()



# tom = Person('Tom', 20)
# bob = Person('Bob', 30)

# tom.display_info()
# bob.display_info()


# Пример 2

# class Pet:

#     def __init__(self, name, age, type, size, weight):
#         self.name = name
#         self.age = age
#         self.type = type
#         self.size = size
#         self.weight = weight

#     def display_info(self):
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Type: {self.type}')
#         print(f'Size: {self.size}')
#         print(f'Weight: {self.weight}')

# pet1 = Pet('Пончик', 10, 'stone', '50x50', '1kg')
# pet1.display_info()

# pet2 = Pet('sdfgsd', -10000, 'stone', 50000000000000000, 2000000000000)
# pet2.display_info()

# Пример 1 с Инкапсуляцией

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1

#     def set_age(self, age):
#         if 1 <= age <= 100:
#             self.__age = age
#         else: print('Недопустимый возраст')
    
#     def get_age(self): return self.__age

#     def get_name(self): return self.__name

#     def display_info(self):
#         print(f'Name: {self.__name}')
#         print(f'Age: {self.__age}')

# tom = Person('Tom')
# tom.display_info()
# print(tom.get_name())
# tom.__age = 30
# print(tom.get_age())
# tom.set_age(30)
# print(tom.get_age())
# tom.set_age(-3000)
# tom.set_age(50)
# tom.display_info()
# tom.age = 20
# tom.display_info()
# print(tom.get_name())


# Аннотации

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1

#     @property # геттер
#     def age(self): return self.__age

#     @age.setter
#     def age(self, age):
#         if 1 <= age <= 100: self.__age = age
#         else: print('Недопустимое значение')

#     @property
#     def name(self): return self.__name

#     def display_info(self):
#         print(f'Name: {self.__name}')
#         print(f'Age: {self.__age}')
    
# tom = Person('Tom')
# tom.display_info()
# print(tom.name)
# print(tom.age)
# tom.age = 0
# tom.display_info()

