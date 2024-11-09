'''Write a program to find out whether a student has passed or failed if it requires a
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
take marks as an input from the user.'''


# Taking input for each subject
Hindi = int(input("Enter your Hindi marks: "))
Marathi = int(input("Enter your Marathi marks: "))
English = int(input("Enter your English marks: "))

# Calculating the total and percentage
total_marks = Hindi + Marathi + English
whole_marks = 300  # Assuming each subject has a maximum of 100 marks

# Calculating percentage
percentage = (total_marks / whole_marks) * 100

# Checking passing criteria
if (percentage >= 40 and Hindi > 33 and Marathi > 33 and English > 33):
    print("You passed with a percentage of:", percentage)
else:
    print("You failed with a percentage of:", percentage)








    

