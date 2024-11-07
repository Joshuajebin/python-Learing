l1 = [10,15,20,25,30]
l2 = [5, 10,15,20,30]

result = list(filter(lambda no:no[0] +no[1] >40, 
            zip(l1,l2)))
print(result)
