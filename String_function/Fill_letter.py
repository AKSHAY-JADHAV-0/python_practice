#Write a program to fill in a letter template given below with name and date
name=input("enter your name: ")
date=str(input("enter your date: "))

print("""
letter='''
        Dear {},
        you are selected
        Date {},
'''
""".format(name,date))