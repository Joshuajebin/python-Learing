no = 153
no2 = no
armstrong = 0
while no>0:
    rem = no%10
    armstrong = armstrong + (rem*rem*rem)
    no = no//10
else:
    if armstrong == no2:
        print("Armstrong")
    else:
        print("Not Armstrong")
