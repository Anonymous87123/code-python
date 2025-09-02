class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."
my_object = MyClass("John", 25)
print(my_object)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
person1 = Person("John", 25)
person1.greet()

class age_contrast:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age
age1 = age_contrast(25, "John")
age2 = age_contrast(35, "Jane")
print(age1 < age2)
print(age1 <= age2)
print(age1 == age2)

class Phone:
    __current_voltage = 5
    def __keep_single_core(self):
        print("Keeping single core")
    def call_by_5g(self):
        if self.__current_voltage == 5:
            print("Calling by 5G")
        else:
            self.__keep_single_core()
            print("Not enough power,已开启单核模式")
phone = Phone()
phone.call_by_5g()

class using_5g:
    __is_5g_enabled = False
    def __check_5g(self):
        if self.__is_5g_enabled == True:
            print("5G is already enabled")
        else:
            print("5G is not enabled.")
    def call_through_5g(self):
        choose = input("Do you want to enable 5G? (yes/no): ")
        if choose == "yes":
            global __is_5g_enabled
            self.__is_5g_enabled = True
        else:
            global __is_5g_enabled
            self.__is_5g_enabled = False
        self.__check_5g()
        print("Calling through 5G")
using_5g = using_5g()
using_5g.call_through_5g()
