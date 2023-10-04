import tkinter as tk
app=tk.Tk()
app.geometry('400x400')
app.resizable('False','False')#(it doesn't support maximixing)
def buttontoclick():
    print('You just clicked me')
frame=tk.Frame(app)
frame.pack()
mylabel=tk.Label(frame,font=('Arial',12,'bold'), text= 'My Button Label', foreground= 'white', width=60,height=5,bg='red')
mylabel.pack()
button=tk.Button(frame,command=lambda:buttontoclick(),font=('Arial',12,'bold'), text= 'Mybutton', background='black',  foreground= 'white')
button.pack(pady=10)
button1=tk.Button(frame,command=lambda:buttontoclick(),font=('Arial',12,'bold'),text='Mybutton',background='black',foreground='white',)
button1.pack(pady=10)
button2=tk.Button(frame,command=lambda:buttontoclick(),font=('Arial',12,'bold'),text='Mybutton',background='black',foreground='white')
button2.pack(pady=10)
button3=tk.Button(frame,command=lambda:buttontoclick(),font=('Arial',12,'bold'),text='Mybutton',background='black',foreground='white')
button3.pack(pady=10)
button4=tk.Button(frame,command=lambda:buttontoclick(),font=('Arial',12,'bold'),text='Mybutton',background='black',foreground='white')
button4.pack(pady=10)
app.mainloop()

x=lambda a:a+10
print(x(5))

def func(n): 
    return lambda a:a*n
mynewout = func(12)
print(mynewout(6))

def newfunc(s):
    return lambda a, b,c: a * b + c + s
newfuncs =  newfunc(10)
print(newfuncs(20, 12,3))