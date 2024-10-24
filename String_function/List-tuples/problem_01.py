#Write a program to store seven fruits in a list entered by the user.

fruits = []
input("Enter the names of fruits (type 'done' to finish):")

while True:
    fruit = input()  # Read input for each fruit
    if fruit.lower() == 'done':
        break
    fruits.append(fruit)  # Append each fruit to the fruits list

print(fruits)  # Print the final list of fruits
