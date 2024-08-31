no=1234
sum_of_digit=0
while no>0:
    
    sum_of_digit= (sum_of_digit*10)+no%10         
    no=no//10
else:
    print(sum_of_digit)
