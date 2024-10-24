# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

# Try to modify an element in the tuple
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error when trying to modify an element: {e}")

# Try to add an element to the tuple
try:
    my_tuple.append(6)
except AttributeError as e:
    print(f"Error when trying to add an element: {e}")

# Try to remove an element from the tuple
try:
    del my_tuple[1]
except TypeError as e:
    print(f"Error when trying to delete an element: {e}")

# Print the original tuple to show it remains unchanged
print("Original tuple:", my_tuple)
