import copy
a = [10,20,30]
b = copy.copy(a)

print(id(a))
print(id(b))

a[2] = 200
print(a[2])
print(b[2])
print(a)
print(b)
