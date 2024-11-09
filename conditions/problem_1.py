'''1. Write a program to find the greatest of four numbers entered by the user.'''

list1 = []

a1 = int(input("enter your number 1: "))
a2 = int(input("enter your number 2: "))
a3 = int(input("enter your number 3: "))
a4 = int(input("enter your number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("a1 is grater: ")

if(a2>a1 and a2>a3 and a2>a4):
    print("a2 is grater: ")

if(a3>a1 and a3>a2 and a1>a4):
    print("a3 is grater: ")

if(a4>a1 and a4>a2 and a4>a3):
    print("a4 is grater: ")