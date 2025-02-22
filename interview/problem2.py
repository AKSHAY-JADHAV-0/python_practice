'''find factorinal of list [12, 13, 50, 25, 30, 45, 1] find two highest number and multiply two numbers'''

nums = [12, 13, 50, 25, 30, 45, 1]

def multiply_highest_two():
    nums.sort(reverse=True)  # Sort the list in descending order
    return nums[0] * nums[1]  # Multiply the two largest numbers

result = multiply_highest_two()
print(f"The product of the two highest numbers: {result}")


