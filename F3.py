#Multiplication from N to 1 (Reverse logic)
#Start from the entered number and decrease it until 1.
n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact *= n
    n -= 1

print("Factorial =", fact)