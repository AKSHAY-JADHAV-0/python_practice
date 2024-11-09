'''Write a program to find whether a given username contains less than 10
characters or not.'''

user_name = input("Enter your username: ")

if len(user_name) < 10:
    print("your username is not valid", user_name)
    print("please enter username at least 10 characters")
else:
    print("your username is valid", user_name)