#!/usr/bin/env python3
# author: bytes-of-tsena

# algorithm:
# read the cipher text from the file(./message.txt in this case )
# split the cipher text by spaces
# using a list comprehension, convert each character to a number then take the modulo of the result with 37
# using a generator expression:
#       - if the number is less than 26, add 65 to the number and convert it to an ascii uppercase character
#       - if the number is less than 36, add 22 to the number and convert it to an ascii digit
#       - if the number is 36, convert it to an underscore
# join the resulting characters from the generator expression to form the plain text
# print the plain text

def main():
    with open("./message.txt", "r") as f:
        cipher_text = f.read().split()
    plain_text = "".join((
        chr(i + 65) if i <= 25 else chr(i + 22) if i <= 35 else "_" for i in list(int(i) % 37 for i in cipher_text)
    ))
    print(plain_text)


if __name__ == "__main__":
    main()
