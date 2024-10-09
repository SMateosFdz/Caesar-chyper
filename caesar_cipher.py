# Simple program to decipher and encrypt Caesar cipher, cyclical
# only ASCII characters
# Input validation: doesn't accept text in number inputs or empty text to encrypt/decipher

#Variables used in encrypt / decipher
value = 0
result = ""
pos = -1
text = ""

while value != 1 and value != 2:
    print("1 - Encrypt or 2 - decipher ")
    try:
        value = int(input())
    except ValueError:
        print("Error, not a number.")

if value == 1: #encryption code
    
    while len(text) == 0:
        print("Write the original text:")
        text = input()
        if len(text) == 0:
            print("Text is empty.")


    while pos < 0:
        print("Number of positions:")
        try:
            pos = int(input())
        except ValueError:
            print("Error, not a number.")

    for i in text:
        if ord(i) == 57:
            x = 48 + pos - 1 #the rotation to the first letter is one position
        elif ord(i) == 90:
            x = 65 + pos - 1 
        elif ord(i) == 122:
            x = 97 + pos - 1
        else:
            x = ord(i) + pos

        x = chr(x)
        result += str(x)

elif value == 2: #decryption code
    while len(text) == 0:
        print("Write the cipher text:")
        text = input()
        if len(text) == 0:
            print("Text is empty.")

    while pos < 0:
        print("Number of positions:")
        try:
            pos = int(input())
        except ValueError:
            print("Error, not a number.")

    for i in text:
        if ord(i) == 57:
            x = 48 + pos - 1
        elif ord(i) == 90:
            x = 65 + pos - 1 
        elif ord(i) == 122:
            x = 97 + pos - 1
        else:
            x = ord(i) + pos

        x = chr(x)
        result += str(x)

print(result)