'''Write a program to calculate the factorial of a given number using for loop.'''

n = int(input("give me your number: "))

result = 1

while n > 0:
    result *= n
    n -= 1 
print(result)
