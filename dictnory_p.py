my_dict = {'name': 'Alice', 'age': 24, 'city': 'New York'}

# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'
print("After adding email:", my_dict)

# Getting a value with a default
age = my_dict.get('age', 'Unknown')
print("Age:", age)

# Removing a key-value pair
removed_value = my_dict.pop('city', 'Not Found')
print("After removing city:", my_dict)
print("Removed value:", removed_value)
