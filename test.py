class Person(object):
    def _init_(self, name, id):
        self.name = name
        self.id = id
    def Display(self):
        print(self.name, self.id)
emp = Person("Jagjit", 102)
emp.Display()

# single inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")

class Child(Parent):
    def func2(self):
        print("This function is in child class.")
object = Child()
object.func1()
object.func2()

# multiple inheritance
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Jasbir"
s1.mothername = "Bhupinder"
s1.parents()


# polymorphism
def add(x, y, z=0):
    return x + y + z
print(add(2, 3))
print(add(2, 3, 4))
# polymorphism
class Human:
    def intro(self):
        print("hello Human")
    def flight(self):
        print("humans can fly fights")
class pilot(Human):
    def flight(self):
        print("Pilots can fly")
class airhostess(Human):
    def flight(self):
        print("airhostess do not fly")
obj_hum = Human()
obj_pil = pilot()
obj_ah = airhostess()
obj_hum.intro()
obj_hum.flight()
obj_pil.intro()
obj_pil.flight()
obj_ah.intro()

#modules

from math import *
print("The value of pi is", pi)
import os
cwd = os.getcwd()
print("Current working directory:", cwd)
from datetime import date
my_date = date(2022, 7, 20)
print("Date", my_date)