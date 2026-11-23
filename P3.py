#Using while loop
n = int(input("Enter number: "))
i = 2

if n <= 1:
    print("Not Prime")
else:
    while i < n:
        if n % i == 0:
            break
        i += 1

    if i == n:
        print("Prime")
    else:
        print("Not Prime")