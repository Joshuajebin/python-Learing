from functools import reduce
names_list = ['raja','kumar', 'kathiravan']
#Max. length 

result = reduce(lambda name1, name2: name1 if len(name1)>len(name2) else name2, names_list)
print(result)
