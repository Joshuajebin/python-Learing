a = [10,20,30]


b = a

print(id(a))
print(id(b))

a[2] = 200
print(a[2])
print(b[1])
print(a)
print(b)
