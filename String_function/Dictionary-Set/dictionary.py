# Creating a dictionary dict1
dict1 = {"akshay": 28, "vishal": 29, "aman": 32, "sameer": 22}
print(type(dict1))  # Output: <class 'dict'>

# Creating another dictionary 'a' with various types of values
a = {"name": "harry", "from": "india", "marks": [92, 98, 96]}
print(type(a))  # Output: <class 'dict'>

# Reading all items (key-value pairs) from dictionary 'a'
read = a.items()
print(read)  # Output: dict_items([('name', 'harry'), ('from', 'india'), ('marks', [92, 98, 96])])

# Reading all keys from dictionary 'a'
keys = a.keys()
print(keys)  # Output: dict_keys(['name', 'from', 'marks'])

# Updating dictionary 'a' with a new key-value pair
a.update({"friends": "myfriend"})
print(a)  # Output: {'name': 'harry', 'from': 'india', 'marks': [92, 98, 96], 'friends': 'myfriend'}

# Retrieving the value associated with the key 'name'
get_value = a.get("name")
print(get_value)  # Output: harry
