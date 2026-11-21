#Using reduce()
from functools import reduce

n = int(input("Enter number: "))

fact = reduce(lambda x, y: x * y, range(1, n + 1), 1)

print(fact)