#VARIABLE MANIPULATION
a=100
b=300
c=20000.008
d=3+1j
print(a)
print(b)
print("My float is", c ,"my complex num is:",d)
#to check the type of a variable
a=100
b=300
c=20000.008
d=3+1j
print("My data type is :",type(a))
print("My data type is :",type(b))
print("My data type is :",type(c))
print("My data type is :",type(d))
#VALUE MANIPULATION
print(100+300)
#CONCATENATION
name='jerry'
age=20
print('the name of the boy is',name, 'and he is',age,  'years old')
#UNPACKING
names=['jerry','caleb','joshua']
a,b,c=names
print(a,b,c)
#END OF UNPACKNG
#CONVERTING FROM STRING TO INT
age='10'
myage=int(age)
print(myage,type(myage))
age=30
accountBal=3000.00
school='nile university'
print(school.capitalize())
print(school.upper())
print(school.replace('n','t'))
print(school.endswith('y'))
if school.endswith('n'):
    save=school.replace('n',' ')
    print(save)
else:
    save=school.replace('n',' ')
    print(save)
classes='three hundered level'
converter=int(accountBal)
ageToDecimal=float(age)
print(name + str(age))
print(name , ageToDecimal, converter)

names=['jerry','caleb','joshua']
if 'jerry' in names:
    print('yes the boy',names[:2], 'is in this list')
elif 'jerry' not in names[0:]:
    print('jerry is not in position')
    
#LOOP
for name in names:
    print(names)
    
for name in names:
    print(name)
    
#STRIP METHOD
classes='     three hundred level   '
print(classes.strip())
#GLOBAL VARIABLE
x=1000
def myvar():
    #LOCAL VARIABLE
    x=2000
    print(x)
    
print(myvar())


def newvar(x):
    print(x)
newvar(200)
print(x)

def myvar():
    global x
    x=5000
    print(x)
myvar()

if x== 5000:
    x=5000-1000
    print(x)
    
def myMath(a,b,c):
    return a + b * c
res=myMath(500,600,700)
print('My return value is:',res)

#RANDOMIZE
import random
print(dir(random))

import random as a
res=a.randrange(0,100)
print(res)

fruits='banana'
for x in fruits:
    print(fruits)

fruits='banana'
#X==FRUITS  BUT FOR THE IN, IF X IS A MEMBER OF FRUITS
for x in fruits:
    print(x)
    
fruits='banana'
newfruits=[]
if "banana" not in fruits:
    print('banana is not present')
elif 'banana' in fruits:
    for x in fruits:
       newfruits.append(x)
       print(newfruits)

fruits='banana'
#X==FRUITS  BUT FOR THE IN, IF X IS A MEMBER OF FRUITS
for x in fruits:
    print(x)
    
fruits='banana'
newfruits=[]
if "banana" not in fruits:
    print('banana is not present')
elif 'banana' in fruits:
    for x in fruits:
       newfruits.append(x)
print(newfruits)    
print(len(newfruits))

myoutput=newfruits.copy()
print(myoutput)
if myoutput== newfruits:
    myoutput.extend(newfruits)
    print(myoutput)
    
import random

print(random.randrange(1, 10))