import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

txt='The rain in spain'
x=re.findall('ai',txt)
y=re.findall('portugal',txt)
print(x)
print(y)

txt = "The rain in Spain"
x = re.search("\s", txt)
y=re.search('portugal',txt)
print("The first white-space character is located in position:", x.start())
print(y)

txt="The rain in spain"
x=re.split("\s",txt)
y=re.split('\s',txt,1)
print(x)
print(y)

txt='The rain in spain'
x=re.sub('\s','34',txt)
y=re.sub('\s','34',txt,2)
print(x)
print(y)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
