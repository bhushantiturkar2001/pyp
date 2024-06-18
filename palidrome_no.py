def is_number_palindrome(number):
    return str(number) == str(number)[::-1]

number = int(input("Enter a number: "))
print(f"Is {number} a palindrome? {is_number_palindrome(number)}")
