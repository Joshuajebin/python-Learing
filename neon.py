def  Neon_number(no):

    no2=no*no
    sum_of_digit=0
    while no2>0:
       digit=no2%10
       sum_of_digit+=digit
       no2//=10
    return sum_of_digit

no = int(input("Enter the Number : "))
if  Neon_number(no)==no:
    print(f"{no} is a Neon Number" )
else:
    print(f"{no} is Not a  Neon Number")




 


