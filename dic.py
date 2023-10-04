fruits={
    'Apple':'red',
    'banana':'yellow',
    'mango':"orange",
    'colors' : ['black','pink','blue']
}
print(type(fruits))
print(fruits)
#UPDATING A DICTIONARY
fruits['Apple']='white'
print(fruits)
fruits.update({'mango':'ash'})
print(fruits)
#ACCESSING AN ITEM VALUE
print(fruits["banana"])
#CHECKING THE LENGTH
print(len(fruits))
#LOOPING THROUGH A DICTIONARY
for x in fruits:
    print(x)
#RETURNS EACH ITEM IN A DIC    
myitems=fruits.items()
print(myitems)
#CHECKING THE VALUES IN A KEY
myvalues=fruits.values()
print(myvalues)
#CHECKING IF A KEY IS IN A DICTIONARY 
if 'Apple' in fruits:
    x=fruits.get('Apple')
print(x)
#GETS THE VALUE OF A SPECIFIED KEY
newval=fruits.get('Apple')
print(newval)
#RETURNS THE VALUE OF THE KEYS
mykey=fruits.keys()
print(mykey)
#ADD A NEW ITEM
fruits['lemon']='green'
print(fruits)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

thefamily= {
    "kid1":{
        'nam':'zainab',
        'age':10
    },
    "kid2":{
        'nam':'fatima',
        'age':11
    },
    "kid3":{
        'nam':'sadiq',
        'age':5
    },
}        
print(thefamily)
  