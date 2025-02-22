# Input: Get the number 'n' from the user
n = int(input("Enter a positive integer (n): "))

# Initialize variables
i = 1       # Starting from the first natural number
sum_n = 0   # To store the sum of the numbers

# Check if the input is a natural number
if n <= 0:
    print("The input must be a natural number (positive integer greater than 0).")
else:
    # While loop to calculate the sum
    while i <= n:
        sum_n += i  # Add the current value of i to sum_n
        i += 1      # Increment i to go to the next natural number
    
    # Output the result
    print(f"The sum of the first {n} natural numbers is: {sum_n}")

