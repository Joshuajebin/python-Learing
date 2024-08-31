def gcd(no1, no2):
    if no1<no2:
        small = no1
    else:
        small = no2
    div = 2
    great = 0
    while div<=small:
        if no1%div==0 and no2%div==0:
            great = div
        div+=1
    else:
        print(great)
    
gcd(100,120)
