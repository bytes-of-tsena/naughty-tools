# Problem description ( picoCTF challenge )

Challenge: [_basic-mod1_](https://play.picoctf.org/practice?bookmarked=0&page=1&search=basic-mod1)

Implement a decryption algorithm that does the following:

- Take each number `mod` 37.
- and map it to the following character set:
  - `0-25` is the _alphabet_ (uppercase),
  - `26-35` are the _decimal_ digits,
  - and `36` is an _underscore_.

## Constraints

- Make sure the code uses the least amount of lines of code you can think of.

## Usage

```sh
python3 ./decrypt-harder.py
```
