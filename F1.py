# Multiplication from 1 to N (Forward logic)
# Start from 1 and multiply each number until n.
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)