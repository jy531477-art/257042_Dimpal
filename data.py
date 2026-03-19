'''print("this is python class")
a = "2"
b = 3.5
c = "hello"
d = True
print(a)
print(b )

print(type(a))
print(type(c))
print(type(d))
print(type(b))'''

'''myname = "abc"#lower case
myName = "de"#camel case
_my_name = "fg"#snake case
MyNameIs = "hi"#pascal case
print(myname)
print(myName)
print(_my_name)
print(MyNameIs)'''


'''a = 1.9
print(type(a))

b = 3
print(type(b))

c = True
print(type(c))

d = "hi"
print(type(d))'''
    

'''a = 25
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a / b)
print(a % b)#remainder
print(a//b)# floor division quotient
print(a**b)#exponent

print( a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)'''

'''x = 0
y = 1
print( x and y)
print( x or y)
print( not x)

a = 10
a+= 20
print(a)
a-=10
print(a)
a*=2
print(a)
a/=2
print(a)
a**=2
print(a)

a = [ 1 , 2 , 3]
b = a
c = [ 1 , 2 , 3]
print(a is b)
print(a is c)# different object , same value
print(a is not c)


a = [ 1 , 2, 3, 4,5]
print(5 in a)
print(10 in a )
print(10 not in a)'''


'''a = 10
b = 5
print(a &b)
print(a|b)
print(a^b)#xor
print(~a)#2's compliment

x = 4 + 3j
print(type(x))

a = 1
b = 2
print(a+b)

xYz = "234 is a positive number"
print(type(xYz))'''

'''a = [1 , 2, 3 ,"apple" , "banana"]
b = {2 , 3, 4}
print(type(a))
a.append("grapes")
print(a)
print(type(b))
c = (1 , 2 , "hi")
print(type(c))'''


'''_my_class = "apple"
a1 = 1
a_b = "hi"
MyName = " riya"
print(_my_class, a1, a_b, MyName)'''

#list (it is changeable)
'''a = [1 , 2, 3 ,"apple" , "banana"]
a.append("grapes")
a.append("hi")
a.insert(3,"apurva")
a.insert(6,3)
print(a)

b = [ 25 , 45 , 56]
b.append("hello")
b.insert(3,5)
print(b)


b = (25 , 45 , 56)

print(b)'''

'''my_dict_ = {"name" : "riya" , "age" : 12 ,"city": "gurugram"}
my_dict_["city"] = "dharuhera"
my_dict_["name"] = "yash"

print(my_dict_)

MySet = {1,2,3,4,3,4,5 ,6 , 8 ,5}
print(type(MySet),MySet)'''

'''my_sets = {1 , 2, 3, "riya"}
print(type(my_sets))
print(my_sets)'''

'''list2 = [1 , 2, 3, 4, 5, 6, "apple", "grapes"]
list2.remove("apple")
print(list2)

list3 = [ 3 , 5, 6, 9 , "hi" , " bye"]
list3.pop(0)
print(list3)

list4 = [7,8,9,0,4,3,"fruits","veggies"]
del list4[3]
print(list4)


list5 =[1 ,2,3,4,5,6,"apple","banana","grapes"]
list5.remove("apple")
list5.pop()
list5.pop(3)
del list5[3]
print(list5)'''


'''list6 = [1,2,3,4,5,"hi"]
print(len(list6))#number of elements

list7 = [1,2,3,4,5,6.5]
print(min(list7))#not used for string
print(max(list7))'''


'''age = int(input("enter your age: "))
if age <13:
    print("child")
elif age<20:
    print("teenager")
elif age<=60:
    print("adult")
else:
    print("senior citizen ")'''


'''num = 6
a = int(input("guess a number"))
if num==a:
    print("correct guess")
else:
    print("not correct")'''




'''for i in range(1,6):
    print("*"*i)
for i in range(6,0,-1):
    print("*"*i)'''








'''n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*"*(2*i-1) )'''


'''c = (1,2,3,4)#simple tuple
print(c)
d = (3,4,"hi","bye")#mixed tuple
print(d)
e = (5,)#single tuple
print(e)



tuple1 = (1,2)
tuple2 = (20,30)
print(tuple1+tuple2)#concatination
print(tuple1*4)#repetition


a = (4,5,6,7,8,9)
b = ("apple","banana")
g = ("yo yo")
print(a+b)
print(g*10)
print(b*2)
print(a+g)'''



'''a ="it is a rainy weather \nmr bear is scared to go outside from his shed"
print(a)


b ="it is a rainy weather \tmr bear is scared to go outside from his shed"
print(b)

c ="it is a rainy weather mr bear is scared to go outside from his shed"
print(len(c))
 
d ="it is a rainy weather \nmr bear is scared to go outside from his shed"
print(d.find('a'))

e = "1"
f = "2"
print(e+f)


g = "yo yo honey singh\t"
print(g*5)

h ="it is a rainy weather mr bear is scared to go outside from his shed"
print(h[-11])

i ="it is a rainy weather mr bear is scared to go outside from his shed"
print(i[4:14])

j ="it is a rainy weather mr bear is scared to go outside from his shed"
print("a" in "bear")

k ="it is a rainy weather mr bear is scared to go outside from his shed"
print(k.lower())

l ="it is a rainy weather mr bear is scared to go outside from his shed"
print(l.upper())

m ="it is a rainy weather mr bear is scared to go outside from his shed"
print(m.capitalize())

n ="it is a rainy weather mr bear is scared to go outside from his shed"
print(n.title())

o ="       it is a rainy weather mr bear is scared to go outside from his shed     "
print(o.strip())

p ="it is a rainy weather mr bear is scared to go outside from his shed"
print(p.replace('ear','eye'))

q ="it is a rainy weather \nmr bear is scared to go outside from his shed"
print(d.find('x'))

r ="it is a rainy weather \nmr bear is scared to go outside from his shed"
print(r.count('a'))

s ="it is a rainy weather \nmr bear is scared to go outside from his shed"
print(s.startswith('i'))

t ="  it is a rainy weather mr bear is scared to go outside from his shed"
print(t.lstrip().startswith('i'))

u ="it is a rainy weather \nmr bear is scared to go outside from his shed  "
print(u.rstrip().startswith('i'))  

v = "you are mango"
w = v.split()
print(w)'''




'''a1 = "it is a very cold day \n nice to meet you"
print(a1)

myclass = "it is a very cold day nice to meet you"
print(myclass.upper())

my_class_ = "HELLO NICE TO MEET YOU"
print(my_class_.lower())

MyList = [1,2,3,4,5]
MyList.remove(4)
MyList.pop()
del MyList[2]
print(MyList)

myList = [ 25 , 45 , 56]
myList.append("hello")
myList.insert(3,5)
print(myList)

a2 = "today is wednesday"
print(a2.capitalize())

a3 = "   today is wednesday  "
print(a3.strip())'''




'''rows = 5

for i in range(rows):
    print(" " * (rows - i) + "🎄" * (2 * i + 1))'''




'''x = int(input("enter a number"))
if x>0:
    print("number is a positive")'''


'''age = int(input("enter your age: "))
if age>18:
    print("you are eligible for voting")
else:
    print("not eligible")'''


'''marks_ = int(input("enter your marks out of 100 : "))
if marks_>=90:
    print("A grade")
elif  marks_>=75:
    print("B grade")
elif  marks_>=55:
    print("C grade")
else:
    print("fail")'''



'''print (" the menu : ")
print ("1. burger = 100rs")
print("2. pizza = 210rs")
print("3. pasta = 90rs")
print("4. sandwich = 60rs")

choice = int(input("enter a the number as per you order : "))
if choice == 1:
    print("your order is burger")
    print("you have to pay 100 rs")
elif choice == 2:
    print("your order is pizza")
    print("you have to pay 210rs")
elif choice ==3:
    print("your order is pasta")
    print("ypu have to pay 90rs")
elif choice == 4:
    print("your order is sandwich")
    print("you have to pay 60rs")
else:
    print("no order placed")
    print("you can have tea as complimentary")'''



'''num1 = int(input("enter a number "))
num2 = int(input("enter a number "))
operator = input(("choose the operator from +,-,*,/ : "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("no operation")'''



'''weather = input("mention the weather (sunny , rainy , cold )").lower()
if weather == "sunny":
    print("use sunscreem")
elif weather == "rainy":
    print("carry an umbrella")
elif weather == "cold":
    print("don't go outside , sleep and eat")
else:
    print("enjoy your day , have a nice day")'''

'''traffic_light = input("enter the light colour (red , yellow , green) : ").lower()
if traffic_light=="red":
    print("STOP!!!!")
elif traffic_light=="yellow":
    print("GET READY !!")
elif traffic_light=="green":
    print("GO!")
else:
    print("you are colour blind")'''



'''for i in range(1,11):
    print(i)

for i in range(6):
    print("hello")'''


'''for i in range(1,6):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)'''

'''for i in range(2):
    for j in range(3):
        print("i = ", i, "j =" , j)'''
 
'''fruits = ["grapes", "apples" , "banana","orange"]
for i in fruits:
    print(i)'''

'''it = iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))'''

'''for i in range(1,11):
    print(i)'''

'''n = 10
while n>=1:
    print(n)
    n = n-1'''

'''n =5
for i in range (1,11):
    print(n,"x",i,"=",n*i)'''

'''n = 1
while n<=20:
    if n % 2 == 0:
        print(n , "is a even number")
    n = n+1'''

'''rows = 10
for i in range(1, 11):
    for j in range(i):
        print("*" , end = " ")
    print()'''


'''import pandas as pd
dim = pd.DataFrame([20,30,40,50,60], columns = ['class'])
print(dim)
print(type(dim))


import pandas as pd
d = pd.DataFrame([20,30,40,50] , columns=["marks"])
print(d)'''

'''import pandas as pd
abc = {
    "name": ["riya","neha","arjun","aryan"],
    "age":[20,23,43,25],
    "salary":[10000 , 20000 , 30000, 40000]
}
df = pd.DataFrame(abc)


#print(df.tail(2))

#print(df.head(1))
#print(df.shape)
#print(df.columns)
#print(df.rename(columns={'salary': 'payment'}, inplace = True))
#print(df)
print(df.info())

print(df.describe())'''



#create a company where you have employee id, age , salary , joining date, min=15
import pandas as pd
#import os
sunproof = {
    "Name" : ["ajay" , "shena" , "riya","nobita","giyan","sunio","bheem","lucky","sameer","shizuka","shinchan","chutki","raju","alien","actionkamin"],
    "age" : [20 ,39,40,60,65,23,15,67,87,45,65,34,45,63,34],
    "salary" : [10000,2000,46784,28467,57699,4000,200000,5000,4567,23456,45678,34567,2345,1234,90856],
    "joiningdate" : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],

}
data = pd.DataFrame(sunproof)
#print(data)
#print(data.tail(2))

#print(data.head(1))
#print(data.shape)
#print(data.columns)
#print(data.rename(columns={'salary': 'payment'}, inplace = True))
#print(data)
#print(data.info())

#print(data.describe())
data.to_csv('company_1.csv',index=False)#to save a file
df = pd.read_csv(r"C:\Users\admin\Desktop\pythonfiles\company_1.csv")# to open a file
print(df)
#os.startfile(r"C:\Users\admin\Desktop\pythonfiles\company_1.csv")

#print(sunproof)
print(data[['Name','age']])#column
print(data['Name'])

print(data.loc[(data.Name=='sunio')&(data.salary<=10000)])#row (for filteration)

print(data.iloc[10])#index value based

print(data.iloc[5:15:5])

print(data['age']<=50) # value always find in boolean

print(data[data['age']<=50]) # this shows the full details of data age<=50

data_df = data[data['age']<=50]
print(data_df)# whenever we will call this variable it will always show this output

print(data[(data['age']>= 30) & (data["salary"]<=7000)])

print(data.where(data['age'] >=30, other = 'not eligible🚩')) # used to write not eligible where this condition is not satisfied

data['team'] = ['accountant' , 'manager','marketing' , 'marketing' , 'developer' ,'marketing','developer','developer','marketing','boss','hr','ceo','cto','developer','developer' ]
print(data)#to add column

data['bonus'] = data['salary']*2
print(data)

data.loc[len(data)] = ['billu',21,100000,10,'hacker',200000]#to add row
print(data)

data.loc[7,'bonus'] = 456838 
print(data)

data.loc[data.Name == 'billu' , 'bonus'] = 234567
print(data)


data = data.drop(data[data.Name == 'sameer'].index)#to delete
print(data)

data= data.drop('bonus',axis =1 )
print(data)