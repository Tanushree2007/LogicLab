#Using a list and product logic
n = int(input("Enter a number: "))
numbers = list(range(1, n + 1))
fact = 1

for num in numbers:
    fact = fact * num

print("Factorial =", fact)