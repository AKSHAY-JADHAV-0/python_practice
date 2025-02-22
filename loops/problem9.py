'''Write a program to print the following star pattern.
***
* * for n = 3
***'''
# Function to print the pattern

def print_star_pattern(n):
    # Loop through the lines
    for i in range(n):
        if i == 0 or i == n - 1:  # First and last line
            print("*" * n)
        else:  # Middle line
            print("*" + " " * (n - 2) + "*")

# Call the function with n = 3
print_star_pattern(3)
