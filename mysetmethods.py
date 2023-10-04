settcon=set(('jerry1','mercy1','james1','john1','jacob1','jamie1'))
settcon1=set(('jerry1','mercy12','james13','john14','jacob15','jamie16'))
#RETURNS A NEW SET THAT CONTAINS ONLY THE ELEMENTS THAT ARE NOT PRESENT IN BOTH SETS
#THIS WILL KEEP ONLY THE ELEMENT THAT ARE NOT PRESENT IN BOTH SETS
settcon1.symmetric_difference_update(settcon)
print(settcon1)
#RETURNS A NEW SET THAT ONLY CONTAINS THE ITEM THAT ARE PRESENT IN BOTH SETS
z=settcon.intersection(settcon1)
print(z)
x=settcon.intersection(settcon1)
print(x)
#THIS WILL KEEP ONLY THE ITEMS THAT ARE PRESENT IN BOTH SETS
settcon.intersection_update(settcon1)
print(settcon)

myset={'jerry','mercy','james','john','jacob','jamie'}
creatset=set(('jerry1','mercy1','james1','john1','jacob1','jamie1'))
creatset1=set(('jerry11','mercy12','james13','john14','jacob15','jamie16'))
creatset2=set(('jerry111','mercy112','james113','john114','jacob115','jamie116'))
#INSERTS THE VALUES IN SET2 INTO SET1
myset.update(creatset)
print(myset)
#RETURNS A NEW SET WITH ALL ITEMS WITH BOTH SETS
mysets=myset.union(creatset).union(creatset1).union(creatset2)
print(mysets)
#RETURNS TRUE WHEN THE ITEMS IN 1ST AND 2ND SETS ARE NOT THE SAME
names={'zainab','fatima','sadiq','faisal'}
age={'12','23','45','56'}
y=names.isdisjoint(age)
print(y)
#RETURNS TRUE IF ALL ITEMS IN THE SET EXISTS IN THE SPECIFIED SET
let={'a','b','c'}
let1={'a','b','c','d','e'}
m=let.issubset(let1)
print(m)
#returns True if all items in the specified set exists in the original set 
n=let.issuperset(let1)
print(n)
#RETURNS A SET THAT CONTAINS THE ITEM THAT ONLY EXISTS IN 1ST SET NOT IN 2ND SETS
creatset.difference(creatset1)
print(creatset)
#REMOVES THE ITEMS THAT EXISTS IN BOTH SETS
creatset.difference_update(creatset1)
print(creatset)
#RETURNS A NEW SET THAT CONTAINS ONLY THE ELEMENTS THAT ARE NOT PRESENT IN BOTH SETS
z=creatset.symmetric_difference(creatset1)
print(z)
#THIS WILL KEEP ONLY THE ELEMENT THAT ARE NOT PRESENT IN BOTH SETS
settcon1.symmetric_difference_update(settcon)
print(settcon1)