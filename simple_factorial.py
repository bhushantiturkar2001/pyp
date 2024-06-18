def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print(f"Factorial of {number} is: {result}")
