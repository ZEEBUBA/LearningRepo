
m=open('country.txt','r')
print(m.read())
m.close()


r=open('country.txt','a')
r.write('you will be rich')
r.close()


x=open('country.txt','r')
print(x.read())

f=open('myfile.txt','x')
f.close()

s=open('myfile.txt','a')
s.write('you are on the right track')
s.close()

p=open('myfile.txt','r')
print(p.read())

my=open('trial.txt','x')
my.close()

res=open('trial.txt','a')
res.write('lalalalala')
res.close()

z=open('trial.txt','r')
print(z.read())
