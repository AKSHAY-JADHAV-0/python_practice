# Initial list
list1 = ["harry", 0.1, 22, 21, "akshay", "priya"]
print(list1)  # Output: ["harry", 0.1, 22, 21, "akshay", "priya"]

# Accessing the first and last elements
first_element = list1[0]
last_element = list1[-1]
print("First element:", first_element)  # Output: "harry"
print("Last element:", last_element)    # Output: "priya"

#################
# Indexing in python
characters = list1[-1]  # Correctly accessing the last element of list1
print(characters)  # Output: "priya"

################
# Adding elements
list1.append("krishna")  # Append adds an element to the end of the list
print(list1)  # Output: ["harry", 0.1, 22, 21, "akshay", "priya", "krishna"]

#####################
# Insert element between strings
list1.insert(1, "Marry")  # Insert "Marry" at index 1
print(list1)  # Output: ["harry", "Marry", 0.1, 22, 21, "akshay", "priya", "krishna"]

#####################
# Remove an element
list1.remove(0.1)  # Remove the first occurrence of 0.1 from the list
print(list1)  # Output: ["harry", "Marry", 22, 21, "akshay", "priya", "krishna"]

#############
# Sort the list
# Sorting will not work because the list has mixed data types (str, int, etc.)
# Let's sort a list that contains only strings or numbers
# Sorting strings in reverse alphabetical order
only_strings = ["harry", "akshay", "priya", "krishna", "Marry"]
only_strings.sort(reverse=True)
print(only_strings)  # Output: ['priya', 'krishna', 'marry', 'harry', 'akshay']

# If you want to sort the original list that contains mixed data types,
# you need to ensure all elements are of the same type or skip sorting entirely.
#create list for square
list2 = [1,2,3,4,5,6,7,8,9,10]
square = [x**2 for x in range(0,9)]
print(square)

#creating list of even no
even = [x for x in range(0,9) if x % 2 == 0]
print(even)

#split sentence
sentence = "Python is fun"
words = sentence.split()
print(words)  # Output: ['Python', 'is', 'fun']

#jion sentence
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # Output: "Python is fun"

#Will delete element at index 2 and return its value
l1 = [1,8,7,2,21,15]
delete = l1.pop(2)
print(l1)