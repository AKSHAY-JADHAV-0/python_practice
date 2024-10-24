'''Write a program to input eight numbers from the user and display all the unique numbers (once).'''

# Get user input as a list of numbers (separated by space)
numbers = input("Write your numbers (separated by space): ")

# Split the input string into a list of numbers
number_list = numbers.split()

# Convert list to set to remove duplicates
unique_numbers = set(number_list)

print(unique_numbers.union())


# Compare lengths to check if any numbers were repeated
#if len(number_list) == len(unique_numbers):
    #print("All numbers are unique, no repetitions.")
#else:
    #print("There are repeated numbers in your input.")




