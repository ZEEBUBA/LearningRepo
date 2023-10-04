def myrecursive(mynum):
    if(mynum > 0):
        result = mynum + myrecursive(mynum-1)
        return result
    else:
        result = 0
        return result
print(myrecursive(6))


def myrecur(number):
    if(number > 0):
        result = number + myrecur(number-1)
        return result
    else:
        result = 0
        return  result
print(myrecur(10))

def recursive(a):
    if a>0:
#10+9+8+7+6+5+4+3+2+1+0
        res=a+recursive(a-1)
        return res
    else:
        return 0
print(recursive(10))

#using recursion,write a program that will do the multiplication of 
#5! and sum it with the value 300

def recursive(num):
    if num>0:
        res=num*recursive(num-1)
        myres=res+300
        return myres
    else:
        return 1
print(recursive(5))


