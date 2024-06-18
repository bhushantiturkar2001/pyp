def is_string_palindrome(string):
    return string == string[::-1]

string = input("Enter a string: ")
print(f"Is '{string}' a palindrome? {is_string_palindrome(string)}")
