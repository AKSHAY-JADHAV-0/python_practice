'''Attempt problem 1 using while loop.'''
'''problem1= Write a program to print multiplication table of a given number using for loop.'''

numbers = int(input("Give me your number: "))

print(f"Multiplication table for {numbers}:")

i = 1  # Initialize the counter
while i <= 10:  # Loop until i reaches 10
    print(f"{numbers} x {i} = {numbers * i}")
    i += 1  # Increment the counter
