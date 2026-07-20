height = int(input("enter height : "))
for i in range(1,height +1):
    for y in range(i):
        print ('*', end=' ')
    print()

for i in range(height,0, -1):
    for y in range(i):
        print('*', end= ' ')
    print()
