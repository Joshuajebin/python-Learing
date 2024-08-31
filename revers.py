no = 123456
no2 = no
reverse = 0
while no>0:
    #rem = no%10
    reverse = (reverse*100) + no%100
    no = no//100
else:
    print(reverse)
