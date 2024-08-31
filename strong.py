def find_fact(num):
    fact = 1
    while num>0:
        fact = fact * num
        num-=1
    return fact


def split(no):
    total = 0
    while no>0:
        rem = no%10 #5  4   1
        total = total + find_fact(rem)
        no=no//10
    return total

no = int(input("Enter the Number : "))
result = split(no)
if no == result:
    print("Strong Number")
else:
    print("Not Strong Number")

