def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    total = sum(int(digit) ** num_len for digit in num_str)
    return total == number

number = int(input("Enter a number: "))
print(f"Is {number} an Armstrong number? {is_armstrong(number)}")
