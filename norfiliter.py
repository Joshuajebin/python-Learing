def find_values(no):
    if no%30 == 0:  
        return no
    else:
        return 0


l = [10,20,30,40,50,60,70,80,90,100]
for no in l:
    print(find_values(no))
