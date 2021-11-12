text = str((input("Masukan Kata : ")))
number = int(input("Masukan Angka : "))

def chiper(text, number):
    result = ""
    for i in text:
        char = i

        if (char.isupper()):
            result += chr((ord(char) + number - 65) % 26 + 65)
        elif char == " ":
            result += " "
        else:
            result += chr((ord(char) + number - 97) % 26 + 97)
    return result

print(chiper(text,number))