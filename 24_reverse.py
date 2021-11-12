kata =  str(input("Masukkan Kata: "))

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

print(reverse(kata))