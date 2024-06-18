# File operations in Python

# Step 1: Create a file and write to it
def create_and_write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
    print(f"File '{file_name}' created and written to.")

# Step 2: Read from the file
def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    print(f"Content of '{file_name}':\n{content}")

# Step 3: Append to the file
def append_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
    print(f"Content appended to '{file_name}'.")

# Example usage:
file_name = 'example.txt'

# Create and write to the file
initial_content = "This is the initial content of the file.\n"
create_and_write_file(file_name, initial_content)

# Read from the file
read_file(file_name)

# Append to the file
additional_content = "This is the appended content of the file.\n"
append_to_file(file_name, additional_content)

# Read from the file again to verify the append operation
read_file(file_name)
