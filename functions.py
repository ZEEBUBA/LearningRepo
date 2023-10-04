def myfunc(a,b):
    return a*b
print(myfunc(10,20))

def myname():
    return 'Hello Today'
print(myname())

def myage(name,age):
    return f"My name is {name} and my age is {age}"
print(myage('Zainab',10))

def myleg(age):
    return f'my age is {age}'
print(myleg(25))

def mynum(num1,num2):
    return num1*num2
print(mynum(23,34))

def myval(num1,num2):
    print('My num is:',num1+num2)
myval(10,20)

def newval(num1,num2):
    num1=20
    num2=30
    print(num1 + num2)
newval(num1=50,num2=20)

def newval(num11,num12):
    print(num11 + num12)
newval(num11=50,num12=20)

def newval():
    return 30+10
print(newval())

def myval():
    print('My name is zee')
myval()

def myval():
    return 'my name is zee'
print(myval())
print(myval())

def myval(let,let1):
    print(let+let1)
myval(23,4)

def func(fname):
    print(fname, 'james')
func('Jerry')
func('John')
func('Fav')
#ARBITRARY ARGUMENT
def func(*fname):
    print(fname, 'james',type(fname))
func('Jerry','John','Fav')
print(type(func))

def func(*fname):
    print(*fname, 'james',type(fname))
func('Jerry','John','Fav')
print(type(func))

def func(*fname):
    print(fname[1], 'james')
func('Jerry','John','Fav')

#KEYWORD ARGUMENT
def func(fname,lname):
    print('My first name is', fname, 'and my last name is', lname)
func(fname='James',lname='Jerry')

#ARBITRARY KEYWORD ARGUMENT
def func(**fullname):
    print('My full name is',fullname, type(fullname))
func(fname='James',lname='Jerry')
'''
#Using a function create an input field that
#will automatically generate the scores gotten by a student,if the questions are fifteen
#in number and the marks each question is 6
#CLUE
15 quetions
 6 marks assigned
 each question is 6 marks
 correct questions answered *6
'''

def myscore():
    while(True):
        score=int(input('Enter the number of quetions answered '))
        if score<16:
            print(score*6)   
        else:
            print('Number of quetions answered exceeded')
myscore()


def password():
    while(True):
        realpassword=input('Enter the correct password')
        if realpassword=="Zainab":
            print('Password Successful')
        else:
            print('Password not successful')
password()
    