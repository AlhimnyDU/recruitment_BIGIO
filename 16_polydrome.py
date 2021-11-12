kata = []
print("Masukan kata satu persatu, untuk berhenti silahkan ketikan 'stop'")
while True:
    x = input("Masukan Huruf: ")
    if x == "stop":
        break
    else:
        kata.append(x)
print()
print(len(kata))
print()
for i in range(len(kata)):
    print(kata[i], end="")
    if(i == len(kata)-1):
        j = i - 1
        while j >= 0 :
            print(kata[j], end="")
            j-=1

