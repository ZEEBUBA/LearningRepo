x=400
def func():
    def myfunc():
        x=455
        print(x)
    myfunc()  
print(x)    
func()   

x=500
def mum():
    global x
    x=2000
mum()    
print(x)

    