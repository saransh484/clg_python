mydict = { 1: 'One' , 2: 'Two' , 3: 'Three'}

print(mydict)
mydict[4] = 'Four'
print(mydict)

mydict[2] = 'NewTwo'
print(mydict)

print(mydict[3])
print(mydict.values())
print(mydict.keys())
mydict.pop(2)
print(mydict)
mydict.popitem()
print(mydict)
del mydict
print(mydict)

