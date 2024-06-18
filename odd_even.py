def find_odd_even(up_to):
    odd_numbers = []
    even_numbers = []
    for i in range(1, up_to + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    return odd_numbers, even_numbers

up_to = int(input("Enter a number: "))
odd, even = find_odd_even(up_to)
print(f"Odd numbers up to {up_to}: {odd}")
print(f"Even numbers up to {up_to}: {even}")
