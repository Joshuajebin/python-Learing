"""
names_a = ['akil', 'ajay']
names = ['joshua', 'sakthivel', 'jecin',names_a]
print(names)
print(len(names))
..........
q = [60,70,36,57]
h = [40,50,60,78,90]
a = [70,80,90]

l = [q,h,a]
print(len(l))
for exams in l:
    for subject in exams:
        print(subject, end=' ')
    print()
....
q = [60,70,36]
h = [40,50,60]
a = [70,80,90]

l = [q,h,a]

i = 0
while i<len(l):
    print(l[i])
    i+=1
..........
q = [60,70,36,45]
h = [40,50,60,90,100]
a = [70,80,90]

l = [q,h,a]

#print(l[0][0])
#print(l[0][1])
#print(l[0][2])

j = 0
while j<len(l[0]):
    print(l[0][j], end=' ')
    j+=1
print()
j = 0
while j<len(l[1]):
    print(l[1][j], end=' ')
    j+=1
print()
j = 0
while j<len(l[2]):
    print(l[2][j], end=' ')
    j+=1
........

q = [60,70,36,45]
h = [40,50,60,90,100]
a = [70,80,90]

l = [q,h,a]

i = 0
while i<len(l):
    j = 0
    while j<len(l[i]):
        print(l[i][j], end=' ')
        j+=1
    print()
    i+=1
"""
def check_list(lst):
    # Count the occurrences of 19 and 5
    count_19 = lst.count(19)
    count_5 = lst.count(5)

    # Check the conditions
    if count_19 == 2 and count_5 >= 3:
        return True
    else:
        return False

# Test the function
lst = [19, 19, 15, 5, 3, 5, 5, 2]
print(check_list(lst))  # Output: True

