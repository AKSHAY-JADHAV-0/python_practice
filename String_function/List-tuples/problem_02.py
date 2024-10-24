#Write a program to accept marks of 6 students and display them in a sorted manner.
Marks = []

for i in range(6):
    while True:
        try:
            mark = int(input(f"Enter your marks for student {i+1}: "))
            Marks.append(mark)
            break
        except ValueError:
            print("Please enter a valid integer for marks.")

print(f"Current value of marks: {Marks}")

