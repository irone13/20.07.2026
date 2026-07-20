n = int(input("enter the size : "))
for i in range(1, n+1):
    for y in range(1, n+1):
        print(f"{i * y : 4}", end=" ")
    print()
