from threading import *
import time
def f1():
    for x in range(5):
        print(x)
t1 = Thread(target=f1, args=[5], name='thread1')
# t1.start()
def f2():
    for x in range(6, 11):
        time.sleep(3)
        print(current_thread().name, x)
t2 = Thread(target=f2(), name='thread2')
t1.start()
t2.start()
t1.join()
t2.join()
#1
from threading import Thread
def f1(n):
    for x in range(n):
        print(x)
t1 = Thread(target=f1,args=[5])
t1.start()
#2
from threading import*
def f1(n):
    for x in range(n):
        print(current_thread().name,x)
t1 = Thread(target=f1,args=[5], name='thread1')
t1.start()
print(current_thread().name)

#3
from threading import*
def f1(n):
    for x in range(n):
        print(current_thread().name,x)
t1 = Thread(target=f1,args=[5], name='thread1')
t1.start()
print(current_thread().name)

def f2():
    for x in range(6,11):
        print(current_thread().name,x)
t2 = Thread(target=f2, name='thread2')
t2.start()
print(current_thread().name)

#4
from threading import*
import time

def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start=time.time()
t1 = Thread(target=f1,args=[5], name='thread1')
print(current_thread().name)

def f2():
    for x in range(6,11):
        print(current_thread().name,x)
t2 = Thread(target=f2, name='thread2')

t1.start()
t2.start()
t1.join()
t2.join()


#5
from threading import*
class A(Thread):
    def run(self):
        for x in range(5):
            print(x)
ob=A()
ob.start()
class A():
    def run(self):
        for x in range(5):
            print(x)
ob=A()
t1=Thread(target=ob.run)
t1.start()


#6
from threading import*
import time

def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start = time.time()
t1 = Thread(target=f1, args=[5], name='thread1')

def f2():
    for x in range(6,11):
        time.sleep(3)
        print(current_thread().name,x)
t2 = Thread(target=f2, name ='thread2')
def f3():
    while True:
        print('hello')