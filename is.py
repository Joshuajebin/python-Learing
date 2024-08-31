def isupper(name):
    for letter in name:
        if (letter>='A' and letter<='Z'):
            pass
        else:
            return False
    else:
        return True

print(isupper('GIRINATH'))
