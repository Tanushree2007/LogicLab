#Recursive logic (Mathematical formula)
# n! = n *(n-1)!
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

n = int(input("Enter a number: "))
print("Factorial =", fact(n))
