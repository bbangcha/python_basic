var1 = 'true'
var2 = 'False'

print(var1)
print(var2)
print(type(var1))
print(type(var2))

var1 = bool(var1)
var2 = bool(var2)
print(var1)
print(var2)
print(type(var1))
print(type(var2))

print(var1 + var2)