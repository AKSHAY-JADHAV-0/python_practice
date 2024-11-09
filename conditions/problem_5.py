'''Write a program which finds out whether a given name is present in a list or not.'''

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Helen", "Ivy", "Jack"]

inputs = input("Search your name: ")

# Check if the input name is in the list
if inputs in names:
    print("Your name is available", inputs)
else:
    print("Your name is not in the list", inputs)
