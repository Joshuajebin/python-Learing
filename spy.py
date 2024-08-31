'''
num=int(input("Enter your number:"))
sum=0
product=1
 
while num>0:
    no=num%10
    sum=sum+no
    product=product*no
    num=num//10
    
 
if(sum==product):
    print("sum:",sum)
    print("product:",product)
    print("It is spy number")
else:
    print("sum:",sum)
    print("product:",product)
    print("So it is not a Spy number!")
'''
def check_spy_number(num):
    sum_digits = 0
    product_digits = 1
    
    while num > 0:
        digit = num % 10
        sum_digits += digit
        product_digits *= digit
        num //= 10
    
    return sum_digits, product_digits

# Main program
num = int(input("Enter your number: "))
sum_digits, product_digits = check_spy_number(num)

print("Sum of digits:", sum_digits)
print("Product of digits:", product_digits)

if sum_digits == product_digits:
    print("It is a Spy number!")
else:
    print("It is not a Spy number!")

