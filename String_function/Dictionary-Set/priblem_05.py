'''Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique.'''

my_dict = {}

name = input("Enter your name: ")
lan = input("Enter your language: ")
my_dict.update({name:lan})

name = input("Enter your name: ")
lan = input("Enter your language: ")
my_dict.update({name:lan})

name = input("Enter your name: ")
lan = input("Enter your language: ")
my_dict.update({name:lan})

name = input("Enter your name: ")
lan = input("Enter your language: ")
my_dict.update({name:lan})

print(my_dict)


