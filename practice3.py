age=30
name= f"My name is Zainab {age}"
print(name)

age=40
name="My age is {}"
print(name.format(age))

goodsname="car"
size=23
price=345.32
goodsitems="My goodsname is {1} and size is {0} and price of goods is {2}"
print(goodsitems.format(goodsname,size,price))

goodsname="car"
size=23
price=345.32
goodsitems=f"My goodsname is {goodsname} and size is {size} and price of goods is {price}"
print(goodsitems)

#IF ELSE STATEMENT
mylist=['Zainab','Bilal','Sadeeq','Caleb','Amina','Rose','Jamila','Adam','Fatima','Maryam']
print(len(mylist))
if 'Zainab' in mylist:
    x = mylist[:5]
    print("These are the first 5 people in my list:",x)
#OR
if 'Zainab' in mylist:
    print("These are the first 5 people in my list:",mylist[:5])
    print("There are",len(mylist[:5]),"people in my new list")
a=100
a+=1
print(a)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
for i in range(100):
    print (i)
    
for j in range(len(thislist)):
    print (j)
print(thislist.count('apple'))

thislist.insert(2,'c')
print(thislist)

    
a=0
while(a<100):
    print(a)
    a+=1
    
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

yourlist = ["apple", "banana", "cherry"]
newlist=[]
for x in yourlist:
    if 'b' in x:
        newlist.append(x)
        print(newlist)
        

yourlist = ["apple", "banana", "cherry"]
yourlist.reverse()
print(yourlist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thistuple = ("apple", "banana", "cherry")
print(list(thistuple))

mytuple=('zainab','sadiq','bilal')
y=list(mytuple)
y.append('fatima')
mytuple=tuple(y)
print(mytuple)

