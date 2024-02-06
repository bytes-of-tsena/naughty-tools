#!/usr/bin/env python3


def modular_inverse(a: int, m: int) -> int:
    """
    Returns the modular inverse of a mod m if it exists, otherwise -1.
    """
    for i in range(1, m):
        if (a * i) % m == 1:
            return i

    return -1


def decrypt_char(ciphertext: int) -> str:
    inverse = modular_inverse(ciphertext % 41, 41)
    if inverse == -1:
        return ""

    return (
        chr(96 + inverse)
        if inverse <= 26
        else str(inverse - 27) if inverse <= 36 else "_"
    )


def main():
    with open("./message.txt", "r") as f:
        ciphertext = list(map(int, (num for num in f.read().split(" ") if num)))

    print("".join(map(decrypt_char, ciphertext)))


if __name__ == "__main__":
    main()
