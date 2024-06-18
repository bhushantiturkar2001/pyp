file_name = 'example.txt'

# Create and write to a file
with open(file_name, 'w') as file:
    file.write("This is the initial content of the file.\n")

# Read from the file
with open(file_name, 'r') as file:
    content = file.read()
    print("Content of the file after initial write:\n", content)

# Append to the file
with open(file_name, 'a') as file:
    file.write("This is the appended content of the file.\n")

# Read from the file again to verify append
with open(file_name, 'r') as file:
    content = file.read()
    print("Content of the file after append:\n", content)
