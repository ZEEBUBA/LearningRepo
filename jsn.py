import json
x='{"Name":"Zainab","age":"23","city":"Nigeria"}'
y=json.loads(x)
print(y['Name'])

x={
    'Name':'Zainab',
    'age':23,
    'city':'Nigeria'
}
y=json.dumps(x)
print(y)