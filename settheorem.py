
#SETS
myset={'jerry','mercy','james','john','jacob','jamie'}
#creting a set using set constructor
creatset=set(('jerry1','mercy1','james1','john1','jacob1','jamie1'))
creatset1=set(('jerry11','mercy12','james13','john14','jacob15','jamie16'))
creatset2=set(('jerry111','mercy112','james113','john114','jacob115','jamie116'))
mylist=[]
newlist=['mango','banana','apple']
print(myset, type(myset))
print(creatset,type(creatset))
creatset=set(('jerry1','mercy1','james1','john1','jacob11','jamie'))
'''
set items are unordered, unindexed and unchangeable
if you want to change an item you add() and remove() to do so.
'''
#using the add() function
myset.add('faith')
print(myset)
3#using the remove function
myset.remove('jacob')
if 'jerry' in myset:
    print('jerry is in list')
    myset.discard('jerry')
print(myset)
#looping through a set
res=len(myset)
for x in myset:
    print(x)
    mylist.append(x)
print(mylist) 
print(len(myset)) 
ress=mylist
ress.append(res)
print(ress)
myset=set(ress)
print(myset)