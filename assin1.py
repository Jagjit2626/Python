#1
mystr = "hello world"
print(len(mystr))
#sol: 11

#2
a="hello"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
print(a, str(b))
#sol: hello {'h': 1, 'e': 1, 'l': 2, 'o': 1}

#3
mystr="hello"
if len(mystr) > 1:
    print(mystr[:2]+mystr[-2:])
else:
    print("empty string")
#sol: helo

#4
mystr="hello"
x = mystr.replace( "e" , "$")
print(x)
#sol: h$llo

#5
str1 ="hello"
str2="world"
str3 = str2[:2]+str1[2:]+' '+str1[:2]+str2[2:]
print(str3)
#sol: wollo herld

#6
a ="fast"
if len(a) < 3:
    x = a
elif a[-3:] == "ing":
    x = a + "ly"
else:
    x = a + "ing"
print (x)
#sol: fasting

#9
mystr="welcome"
n =3
x= mystr[:n-1] + mystr[n:]
print(x)
#sol: wecome