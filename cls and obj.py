class caleblab:
    x=5
myclass=caleblab
print(myclass.x)

class person:
    def __init__(self,name,age):
        self.myname=name
        self.myage=age
    def __str__(self):
        return f'{self.myname},({self.myage})'
p1=person('zainab',63)
print(p1)

class human:
    def __init__(myvar,name,age):
        myvar.a=name
        myvar.b=age
    def myfunc(myvar):
        print('my age is',myvar.b)
p1=human('john',34)
p1.myfunc()
p1.b=76
print(p1.b)

class subperson(human):
    pass
mysubperson = subperson('jerry',3)
print(mysubperson.a)
print(mysubperson.b)

class secondclass(caleblab):
    pass
mysecondclass = secondclass()
print(mysecondclass.x)

class boy:
    def __init__(newvar,fname,lname):
        newvar.firstname=fname
        newvar.lastname=lname
    
class student(boy):
    def __init__(newvar,fname,lname, gradyear):
        super().__init__(fname,lname)
        newvar.year = gradyear
    def printname(newvar):
        print(f'my firstname is : {newvar.firstname}, and my lastname is : {newvar.lastname} and my grad year is : {newvar.year} ')
    
x=student('mike','joel', 2023)
x.printname()

