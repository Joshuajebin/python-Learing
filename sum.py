no=1234
sum_of_digit=0
while no>0:
    rem=no%10
    sum_of_digit= sum_of_digit+rem
    no=no//10
else:
    print(sum_of_digit)
