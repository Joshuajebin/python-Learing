word = 'A5'
first = word[0] #A
second = int(word[1]) #5
for no in range(second):
    print(chr(ord(first)+1))
