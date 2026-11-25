#Using string conversion
n = input("Enter number: ")
power = len(n)
total = 0

for digit in n:
    total += int(digit) ** power

if total == int(n):
    print("Armstrong")
else:
    print("Not Armstrong")