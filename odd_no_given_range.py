def sum_of_odds(up_to):
    return sum(i for i in range(1, up_to + 1) if i % 2 != 0)

up_to = int(input("Enter a range: "))
print(f"Sum of odd numbers up to {up_to}: {sum_of_odds(up_to)}")
