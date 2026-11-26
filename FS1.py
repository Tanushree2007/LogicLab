#Using temporary variable
n = int(input("Enter terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c