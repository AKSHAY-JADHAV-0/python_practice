'''Write a program to find whether a given number is prime or not.'''
numbers = int(input("give me your number: "))

for i in range(1, numbers):
    if (numbers%i) == 0:
        print(f"number is prime {numbers}")
    else:
        print("number is not prime {numbers}")

     