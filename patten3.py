for row in range (1,6):
    for col in range(1,row):
        print(" ",end=" ")
    for col in range(1,7-row):
        print("1",end=" ")
    print()
