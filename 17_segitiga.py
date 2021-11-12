baris = int(input("Masukan Baris Segitiga : "))

def f_triangel(baris):
    a = baris
    s = 0
    for i in range(0, baris):
        for j in range(0, s):
            print(' ',end='')
        s += 1
        for j in range(0, a):
            print("* " , end='')

        a-=1
        print()

    a+=2
    s-=1

    for i in range(0, baris-1):
        for j in range(0, s-1):
            print(' ', end='')
        s -= 1
        for j in range(0, a):
            print('* ', end='')
        a+=1

        print('')

f_triangel(baris)
