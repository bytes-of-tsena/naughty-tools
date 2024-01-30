def decrypt(cipher_text):
    cipher_text = (int(i) % 37 for i in cipher_text)

    # map each number to a character set
    # this is done by adding 97 to the number if it is less than 26, adding 22 to the number if it is less than 36, and adding 0 to the number if it is 36
    # added 22 to number because 26 + 22 = 48, which is the ascii value of 0 and then we carry on from there for all the digits till 9
    cipher_text = (
        chr(i + 97) if i < 26 else chr(i + 22) if i < 36 else "_" for i in cipher_text
    )

    return "".join(cipher_text)


def main():
    with open("./message.txt", "r") as f:
        cipher_text = f.read().split()

    print(decrypt(cipher_text))


if __name__ == "__main__":
    main()
