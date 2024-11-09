'''Write a program to find out whether a given post is talking about “Harry” or not.'''

post = input("Enter your post: ")

# Check if "harry" is in the post (case-insensitive)
if "harry".lower() in post.lower():
    print("This post is about Harry")
else:
    print("This post is not about Harry")
