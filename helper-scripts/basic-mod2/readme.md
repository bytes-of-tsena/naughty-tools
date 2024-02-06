# Problem description( picoCTF challenge )

challenge: [basic-mod2](https://play.picoctf.org/practice?page=1&search=basic-mod2)

Implement a decryption algorithm that does the following:

- Take each number `mod` 41 and find the **modular inverse** for the result.
- Then map to the following character set:
  - `1-26` are the *alphabet*,
  - `27-36` are the *decimal* digits,
  - and `37` is an *underscore*.

## Usage

```bash
python3 decrypt.py
```
