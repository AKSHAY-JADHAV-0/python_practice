'''Write a program using functions to find greatest of three numbers.'''
num_list = list(map(int, input("Enter numbers separated by space: ").split()))

def greatest_num(numbers):
    if len(numbers) < 3:
        return "At least two numbers are required"

    sorted_numbers = sorted(numbers, reverse=True)
    max_num = sorted_numbers[0]
    second_max = sorted_numbers[1] if len(sorted_numbers) > 1 else "No second max"
    third_max= sorted_numbers[2] if len(sorted_numbers) > 2 else "No third max"
    
    return max_num, second_max, third_max

print(greatest_num(num_list))
