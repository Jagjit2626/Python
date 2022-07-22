#Encapsulation
class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()
#abstration
from abc import ABC,abstractmethod
class Car(ABC):
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")
class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")
class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")
t = Tesla()
t.mileage()
r = Renault()
r.mileage()
s = Suzuki()
s.mileage()
d = Duster()
d.mileage()
#try
try:
  print(x)
except:
  print("An exception occurred")
#else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#error raising
x = "hello"
if not type(x) is int:
     raise TypeError("Only integers are allowed")