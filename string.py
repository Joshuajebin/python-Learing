
def isalpha(name):
    for letter in name:
        if letter>='a' and letter<='z'or letter>='A' and letter<='Z' :
            pass
        else:
            return False
    else:
        return True

print(isalpha('akil234'))



"""


name = "JOSHUA"
contains_digit = False

for char in name:
    if char.isdigit():  # Check if the character is a digit
        contains_digit = True
        break  # Stop checking if a digit is found

if contains_digit:
    print(False)
else:
    print(True)
"""
