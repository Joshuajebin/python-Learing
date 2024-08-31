def isalnum(pincode):
    i=0
    while i<len(pincode):
        if pincode>='0' and pincode<='9' or (pincode>='a' and pincode<='z') or (pincode>='A' and pincode<='Z'):
            print(True)
            continue
        else:
            print(False)
        break
    


pincode = "chennai   600042"
isalnum(pincode)
