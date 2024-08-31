def find_perfect(no):
    div = 1
    sum = 0
    while div<no:
        if no%div==0:
            sum+=div
        div+=1
    return sum

no = int(input("Enter no. "))
if no== find_perfect(no):
    print(f"{no} is Perfect")
else:
    print(f"{no} is Not perfect")
