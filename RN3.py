#String concatenation using loop
n = int(input("Enter number: "))
rev = ""

while n > 0:
    digit = n % 10
    rev += str(digit)
    n //= 10

print(rev)