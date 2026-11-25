#Using while loop
n = int(input("Enter number: "))
temp = n
total = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10

if total == temp:
    print("Armstrong")
else:
    print("Not Armstrong")