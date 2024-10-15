students = {}
count = int(input("Enter no. of students: "))
for i in range(count):
    name = input("Enter Name: ")
    roll_no = int(input("Enter Roll no. "))
    students[roll_no] = name

print(students)
