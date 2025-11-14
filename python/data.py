'''a = 23
b=12
print("my age", a)
print(f"my age is{a}years")
print(f"calculate {a+b}")
print(f"this sis floating value {a: .4f}")
txt = "hello"
print(txt.capitalize())
print(txt.center(300))
y=" hi welcome lets learn something enjoyable, nice to meet you all"
print(y.count("e"))
print(y.islower())
y="YEAH"
print(y.isupper())'''
'''a = 12
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
x =10
y = 20
print(x+y)
print(x-y)
print(x*y)
print(x**y)
print(x//y)
print(x/y)
print(12==13)
print(12!=13 , 12==12)
print(12>13)
print(12<13)
print(12<=13)
print(12>=13)
x= 15
print(12<x<13)
print(12<x>13)
print(12<13<x)
print(12<15 and 13>12 or 12==12)
print(134>1344 and 234<546)
print(134>1344 or 234<546)
print(not(12>15 or 15<20))
x = 6# 0110
y = 3#0011
print(x&y)#0010 , if anyone is false the all is false
print(x|y)
print(x^y)
print(x<<2)
print(x>>2)'''
'''a = int(input("enter a number"))
b = int(input("enter again"))
if a>b:
    print("a is greater to b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater the a")'''
'''a = int(input("enter your age:"))
if a>=18:
    print("you are eligible for giving vote")
else:
    print("you are not eligible for voting")'''
'''a =int(input("enter your marks out of 100 :"))
if 35<=a<65:
    print("your grade is C")
elif 65<=a<80:
    print(" your grade is B")
elif 80<=a<90:
    print("your grade is A")
elif a>=95:
    print("your grade ia A++")
else:
    print("you are failed")'''
'''a = int(input("enter a number: "))
b = int(input("enetr second number: "))
if a>b:
    print("a is greater then b")
elif a==b:
    print(" a is equals to b")
else:
    print("b is greater then a")'''
'''a = input("enter your gender as M/m or F/f: ")
if a == 'M' or a=='m':
    print("good morning sir")
elif a =='F' or a=='f':
    print("good morning ma'am")
else:
    print("who are you")'''
'''a=int(input("enter  a number"))
if a%2==0:
    print("a is a even number")
else:
    print("a is a odd number")'''



'''a = int(input("enter the temperature in celcius: "))
if a<0:
    print("temperature is freezing cold")
elif 0<a<=10:
    print("temperature is very cold")
elif 10<a<=20:
    print("temperature is cold")
elif 20<a<=30:
    print("temperature is pleasent")
elif 30<a<=40:
    print("temperature is hot")
else:
    print("temperature very hot")'''


#list are used to store the multiple values in the single variable
#list can store both int and string values
'''a = ["apurva" ," prachi", "nikita", "dimpal", 12]
print(len(a))
print(a[1])
print(type(a))
a[0:2]=["hello","hi","yo"]
print(a)'''


'''#tuples
a =(1,"rachit",True)
print(a)
print(type(a))
print(a[:1])

#sets
a ={1, 2, 3, 4,5, "rachit","vaishnavi"}
print(type(a))


#dictionary
a={"name":"dimpal", "age":18, "college":"ABC"}
print(a)
print(a["college"])'''


#loops
#while loops
'''i = 7
while i < 10:
    i+=1
    print(i)

count = 5
while count>0:
    if count%2 ==0:
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count-=1'''


#for loop
'''nums=[1, 2,3,4,5 ,6,7,8,9]
for num in nums:
    if num %2 ==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")'''
'''for i in range(1, 11):
    print(i)
for i in range(10, 0,-1):
    print(i)
for i in range(5,51,5):
    print(i)'''


'''student_marks ={"prachi": 62 ,"apurva":100, "nikita":80, "rajat":50,"pop":0}
for student,marks in student_marks.items():
    if marks>=90:
        grade ='A+'
    elif marks>=80:
        grade ='A'
    elif marks>=70:
        grade ='B'
    elif marks>=60:
        grade ='C'
    elif marks>=50:
        grade ='D'
    else:
        grade='F'
    print(f"{student} scored{marks} and grade {grade}")'''




'''def abc():
    print("hello world")
abc()
abc()
abc()'''


'''def abc(name):
    print(f"my name is {name}")
abc("apurva")
abc("dimpal")
abc("nancy")'''

'''def square(num):
    return num*num
result = square(5)
print("square is", result)'''

'''def sum(num1 ,num2 ):
    return num1+num2
result = sum(5,6)
print("sum is", result)'''

'''def sub(num1 , num2):
    return num1-num2
result = sub(6,5)
print("sub is", result)



def div(num1 , num2):
    return num1/num2
result = div(25,5)
print("div is", result )'''




#write a python code on book system
#make function and store the data in dictionary atleast five books
#make user call the number of book and that book need to display
'''def abc():
    num_books= {1:"book1" , 2:"book2" , 3:"book3" ,4:"book4" ,5:"book5"}
    n = int(input("enter the number"))
    if n in num_books:
        print(f"the book is{num_books[n]}")
    else:
        print("no books")
abc()
abc()'''




'''def max(a,b):
    if a>b:
        print(f"{a}")
    else:
        print(f"{b}")
max(6,5)
max(1000,10000000)'''




'''def sum_all(*args):
    total = 0
    for i in args:
        total +=i
    return total

print(sum_all(1,2,3,4))'''



#import
'''import person
print(person.greet("riya"))'''

'''import random
print("random number between 1-10:" , random.randint(1,10))
color=["red","blue","green"]
print("colors you choose:",random.choice(color))'''


'''import random
a = random.randint(1,10)
if a%2==0:
    print("you are lucky")
else:
    print("you are not lucky")'''


'''import datetime
today = datetime.date.today()
print("time is", today)

now = datetime.datetime.now()
print("the time is " , now)'''


'''import sys
print("python version", sys.version)
print("platform", sys.platform)'''


'''import math
print ("power", pow(2,3))
print("square rootof 25:" , math.sqrt(25))
print("ceil" , math.ceil(4.3))
print("floor" , math.floor(4.8))
print("value of pi:" , math.pi)'''

'''import random
a = ["angel" ,"demon"]
name =["nancy" , "pinky" , "hgu" , "vrash" ,"cr"]
p =["boil","skin peeling" ,"apple eating" ,"forever walking" ,"no place in heaven" ,"eye plucked off" ]
print("who are you" , random.choice(a))
print("name" , random.choice(name))
print("punisment you will get" , random.choice(p))'''

#create a function take random value using random module
#check of the value is positive or negative and print it
#check if the value is divisible with 5 or not and print it
#check if the number is even or odd

'''import random
def num():
    n = random.randint(-100,100)
    print("genrated value", n)
    if n >0:
       print("number is positive")
    else:
       print("negative")
    if n%5==0:
       print("number is divible by 5")
    else:
      print("not divisible")
    if n%2==0:
      print("number is even")
    else:
      print("number is odd")
num()'''



'''class abc:
    def __init__(self, name , age):
        self.name= name
        self.age = age
p1 = abc("riya" ,18)
print(p1.name,p1.age)'''


#create class named as rectangle
#there is attributes in it length and width
#there is method named as area which return area of rectangle
#get input from user a and b

'''class car:
    def __init__(self,brand,color):
        self.brand= brand
        self.color=color

    def drive(self):
        print(f"{self.color} {self.brand} is driving")
car1 =car("BMW","Black")
car2= car("tesla", "white")

car1.drive()
car2.drive()'''

'''class IceCream:
    def __init__(self ,brand, flavour):
        self.brand=brand
        self.flavour=flavour

    def abc(self):
        print(f"i got {self.brand} of {self.flavour}")
a = IceCream("chocolate","motherdairy")
b= IceCream("strawberry" ,"kawality walls")

a.abc()
b.abc()'''


'''class person:
    def __init__(self,name,age):
        self.name= name
        self.__age=age
p1= person("emilly",23)
print(p1.name)
print(p1.__age)'''



'''class animal:
    def speak(self):
        print("animal speaks")
class dog(animal):
    def speak(self):
        print("dog barks")

dog = dog()
dog.speak()'''




'''class cat:
    def sound(self):
        return "meow"
class dog:
    def sound(self):
        return"woof"
for animal in [cat(), dog()]:
    print(animal.sound()) '''


'''class animal:
    def speak(self):
        print("animal make different sound")
class dog(animal):
    def speak(self):
        print("dog barks")
class cat(animal):
    def speak(self):
        print("cat meows")
for pet in[dog(),cat()]:
    pet.speak()'''

#panda

'''import pandas as pd

data=[10,20,30,40]
s=pd.Series(data)

print(s)'''





'''import pandas as pd

data = {
    'Name':['X' ,' Y' ,'Z','W'],
    'Age': [17 , 15, 18,16],
    'Marks':[85, 95, 42, 87]
    }
df = pd.DataFrame(data)
print(df)
print(pd.__version__)'''


'''import pandas as pd
data = [10,20,30,40]
s=pd.Series(data)
print(s)



import pandas as pd
a= [1,7,2]
myvar= pd.Series(a)
myvar = pd.Series(a,index=['x','y','z'])
print(myvar["y"])
print(myvar)'''


'''
import pandas as pd
calories = {"day1": 420,"day2": 380, "day3": 560}
a = pd.Series(calories)
print(a)
'''



'''import pandas as pd
marks = {"maths": 90 , "science": 80, "english":100}
a = pd.Series(marks)
print (a)
print(a["science"])'''


















