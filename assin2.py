#1 palindrome
num =int(input("Enter any number: "))
reverse = int(str(num)[::-1])
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

#2 factorial
num = 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#3 fibinacci
num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
print()


#5 calculator
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("Select Operation: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
while True:
    choice=input("Enter Choice(1/2/3/4): ")
    if choice in('1','2','3','4'):
        a=float(input("Enter First Number: "))
        b=float(input("Enter Second Nuumber: "))
        if choice=='1':
            print(a, "+", b, "=", add(a,b))
        elif choice=='2':
            print(a, "-", b, "=", subtract(a,b))
        elif choice=='3':
            print(a, "*", b,"=", multiply(a,b))
        elif choice=='4':
            print(a, "/", b, "=", divide(a,b))
        next_calculation=input("Let's do another calculation? (yes/no): ")
        if next_calculation=="no":
            break
    else:
        print("invalid input")


#6 Pattern printing
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

#7 leap year
year = 2000
if (year%400 == 0) or (year%4==0 and year%100!=0):
  print("Leap Year")
else:
  print("Not a Leap Year")


#8 prime no
num=int(input("Enter Number: "))
prime=False
for i in range(2,num):
    if (num%i == 0):
        prime=False
    if num==1:
        print("composite no")
        break
if prime:
    print("prime no")
else:
    print("not prime")
num=int(input("Enter Number: "))

#9 area of triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("The area of the triangle is", area)
