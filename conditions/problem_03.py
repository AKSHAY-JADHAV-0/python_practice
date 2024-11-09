'''A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.'''

# Input for email text
email = input("Enter your email: ")

# List of spam keywords
keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# Check if any keyword is in the email text
if any(keyword.lower() in email.lower() for keyword in keywords):
    print("This is spam mail")
else:
    print("This is not spam mail")

