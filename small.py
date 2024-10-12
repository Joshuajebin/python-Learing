l1 = ['l','b','n']
l2 = ['i','i']
small = len(l1) if len(l1)<len(l2) else len(l2)
#python
for no in range(small):
    print(l1[no]+l2[no],end='')
