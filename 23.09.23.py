'''
class подкласс(суперкласс):
    методы класса

    
isinstance(object, type) - проверка типа обьекта
'''

# Пример без наследования

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self): return self.__name

#     def display_info(self):
#         print(f'Name: {self.__name}')


# class Employee:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self): return self.__name

#     def display_info(self):
#         print(f'Name: {self.__name}')

#     def work(self):
#         print(f'{self.name} works')

# Пример по наследованию

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self): return self.__name

#     def display_info(self):
#         print(f'Name: {self.__name}')


# class Employee(Person):
#     def work(self):
#         print(f'{self.name} works')

# tom = Employee('Tom')
# print(tom.name)
# tom.display_info()
# tom.work()

# Множественное наследие

# class Employee:
#     def work(self): print('Employee works')

# class Student:
#     def study(self): print('Student studies')

# class WorkingStudent(Employee, Student):
#     pass

# tom = WorkingStudent()
# tom.work()
# tom.study()

# Переопределение функционала базового класса

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self): return self.__name

#     def display_info(self):
#         print(f'Name: {self.__name}')


# class Employee(Person):

#     def __init__(self, name, company):
#         super().__init__(name)
#         self.company = company

#     def display_info(self):
#         super().display_info()
#         print(f'Company: {self.company}')

#     def work(self):
#         print(f'{self.name} works')

# tom = Employee('Tom', ' Yandex')
# tom.display_info()

# Проверка типа обьекта

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     @property
#     def name(self): return self.__name

#     def do_nothing(self):
#         print(f'{self.name} does nothing')

# class Employee(Person):
#     def work(self):
#         print(f'{self.name} works')

# class Student(Person):
#     def study(self):
#         print(f'{self.name} studies')

# def act(person):
#     if isinstance(person, Student): person.study()
#     elif isinstance(person, Employee): person.work()
#     elif isinstance(person, Person): person.do_nothing()

# tom = Employee('Tom')
# bob = Student('Bob')
# sam = Person('Sam')
# act(tom)
# act(bob)
# act(sam)