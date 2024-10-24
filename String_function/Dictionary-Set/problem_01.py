"""Write a program to create a dictionary of Hindi words with values as their English translation. 
Provide user with an option to look it up!"""

my_dict = {
    "नाम": "name",
    "आयु": "age",
    "शहर": "city",
    "देश": "country",
    "पेशा": "profession",
    "दोस्त": "friend",
    "पुस्तक": "book",
    "विद्यालय": "school",
    "गाड़ी": "car",
    "फल": "fruit"
}

# Get user input
language = input('Select your language (hindi/English): ').lower()

# Check user input and display appropriate result
if language == 'hindi':
    print("Here are the available Hindi words: ")
    print(', '.join(my_dict.keys()))  # Print the keys (Hindi words)

elif language == 'english':
    print("Here are the available English translations: ")
    print(', '.join(my_dict.values()))  # Print the values (English translations)

else:
    print("Please select the correct option.")
