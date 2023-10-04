x=(3,4,87,3)
y=(2,3,98,54)
print(min(x))
print(max(y))

a=(-34785)
print(abs(a))

b=pow(4, 3)
print(b)

import math
x=math.sqrt(64)
print(x)

x=1.3
y=1.3
print(math.ceil(x))
print(math.floor(y))

x=math.pi
print(x)

    
def num():
     while(True):
        a=int(input('Enter a negative number'))
        if a<1:
            return abs(a)
        else:
            return a
print(num())