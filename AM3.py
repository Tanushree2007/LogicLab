#Using a list
n = int(input("Enter number: "))
digits = list(map(int, str(n)))
power = len(digits)

total = sum(d ** power for d in digits)

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")