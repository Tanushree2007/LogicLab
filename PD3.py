#Using a loop to build reverse
n = int(input("Enter number: "))
temp = n
rev = ""

while n > 0:
    rev += str(n % 10)
    n //= 10

if str(temp) == rev:
    print("Palindrome")
else:
    print("Not Palindrome")