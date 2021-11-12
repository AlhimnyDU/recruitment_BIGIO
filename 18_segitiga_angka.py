a = 9
b = 3
angka = 1

for i in range(0, a):
    for j in range(0, i + 1):
        print(j+1, end='')
    for j in range(0, (a*2)-b):
        print(' ', end='')
    for j in reversed(range(0, i + 1)):
        if a!=j+1:
            print(j+1, end='')
    b+=2
    print('')

b=a+1
for i in range(0, a):
    for j in range(0, a):
        if j!=0:
            print(j, end='')
    for j in range(0, b-a):
        print(' ', end='')
    b+=1

    for j in reversed(range(0, a)):
        if j!=0:
            print(j, end='')

    a -= 1
    print('')
