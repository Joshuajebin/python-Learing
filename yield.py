def first_n_numbers(num):
    no = 1
    while no<=num:
        yield no
        no+=1

result = first_n_numbers(10)
print(type(result))

for value in result:
    print(value,end=' ')
