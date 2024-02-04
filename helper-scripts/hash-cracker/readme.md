# Hash cracker

This is a simple hash cracker that can crack `md5`, `sha1`, `sha256`, `sha384` & `sha512` hashes.

## Pre-requisites

- Python `3.10` or higher (recommended) -- this is *primarily* because of the `match` statement used in the script

## Features

- [x] Crack `md5`, `sha1`, `sha256`, `sha384` & `sha512` hashes

## Installation

```bash
git clone https://github.com/bytes-of-tsena/naughty-tools.git
```

## Usage

```bash
cd naughty-tools/helper-scripts/hash-cracker
python3 hash-cracker.py -h
```

## Example

```bash
python3 hash-cracker.py -t md5 -w ./wordlist.txt -d 098f6bcd4621d373cade4e832627b4f6
```

## License

MIT

## Author

[sena](https://github.com/bytes-of-tsena)
