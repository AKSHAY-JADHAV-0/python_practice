'''Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50=> F'''

marks = int(input("enter your marks: "))

if marks in range(90, 100):
    print("your grade is EX")
elif marks in range(80, 90):
    print("your grade is A")
elif marks in range(70, 80):
    print("your grade is B")
elif marks in range(60, 70):
    print("your grade is C")
elif marks in range(50, 60):
    print("your grade is D")
else:
    print("your grade is F")