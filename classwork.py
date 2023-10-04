mylist=['apple','banana','banana', 'apple', 'watermelon', 'orange', 'pawpaw', 'grapes']
thelist= list(dict.fromkeys(mylist))
print(thelist)
thelist.reverse()
print(thelist)
for x in thelist:
    print (x)
mytuple=tuple(thelist)
print(mytuple)    
if 'banana' in thelist:
    print('These are the last 2 items in the tuple', (thelist[4:6]))
newlist=list(thelist[4:6])
newlist.append('cherry')
newlist.append('mango')
newlist.append('sugarcane')
newlist.append('pineapple')
#i added a new fruit
newlist.apend('pear')
print(newlist)
