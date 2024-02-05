from typing import Iterable


def collect_args():
    import argparse

    parser = argparse.ArgumentParser(
        description="Crack a hash using a wordlist. Created by @bytes-of-tsena",
        add_help=False,
    )
    parser.add_argument(
        "-w",
        "--wordlists",
        required=True,
        help="Wordlist(s) file path with potential passwords to crack hash e.g. /usr/share/wordlists/rockyou.txt or /usr/share/wordlists/rockyou.txt /usr/share/wordlists/wordlist.txt /usr/share/wordlists/wordlist2.txt",
        nargs="+",
    )
    parser.add_argument(
        "-d",
        "--digest",
        required=True,
        help="Digest to crack i.e. hash value of the password e.g. 5f4dcc3b5aa765d61d8327deb882cf99 for 'password'",
    )
    parser.add_argument(
        "-t",
        "--type",
        required=True,
        help="Type of hash to crack i.e. 'md5', 'sha1', 'sha256', 'sha512' (only these 4 types are supported for now)",
    )
    parser.add_argument(
        "-h", "--help", help="Help on how to use the program", action="store_true"
    )

    return parser.parse_args()


def read_wordlist(file_path: str) -> str | None:
    # used a generator to read the file line by line so as to "not" load the entire file into memory
    with open(file_path, "r") as file:
        for word in file:
            yield word.strip()


def crack_hash_multi_wordlists(
    target_hash: str, wordlists: Iterable[str], hash_type: str
) -> tuple[str | None, str]:
    for wordlist in wordlists:
        cracked_hash = crack_hash(target_hash, read_wordlist(wordlist), hash_type)
        if cracked_hash:
            return (cracked_hash, wordlist)

    return (None, "")


def crack_hash(target_hash: str, wordlist: Iterable, hash_type: str) -> str | None:
    import hashlib

    for word in wordlist:
        raw_word = word.encode()
        match hash_type:
            case "md5":
                if hashlib.md5(raw_word).hexdigest() == target_hash:
                    return word
            case "sha1":
                if hashlib.sha1(raw_word).hexdigest() == target_hash:
                    return word
            case "sha256":
                if hashlib.sha256(raw_word).hexdigest() == target_hash:
                    return word
            case "sha384":
                if hashlib.sha384(raw_word).hexdigest() == target_hash:
                    return word
            case "sha512":
                if hashlib.sha512(raw_word).hexdigest() == target_hash:
                    return word
            case _:
                print("Invalid hash type")
                return None


def print_help():
    args = {
        "-w": "Wordlist file path with potential passwords to crack hash e.g. /usr/share/wordlists/rockyou.txt",
        "-d": "Digest to crack i.e. hash value of the password e.g. 5f4dcc3b5aa765d61d8327deb882cf99 for 'password'",
        "-t": "Type of hash to crack i.e. 'md5', 'sha1', 'sha256', 'sha512' (only these 4 types are supported for now)",
        "-h": "Help on how to use the program",
    }

    print_usage()
    for arg, desc in args.items():
        print(f"{arg}: {desc}")


def print_usage():
    print(
        "Usage: python hash-cracker.py -w <wordlist> -d <digest> -t <type>. Use -h for more information."
    )


def main():
    try:
        args = collect_args()

        if args.help:
            print_help()
            return

        if not args.wordlists or not args.digest or not args.type:
            print_usage()
            if not args.wordlists:
                print("-- Error: Wordlist is required")
            if not args.digest:
                print("-- Error: Digest or hash is required")
            if not args.type:
                print(
                    "-- Error: Type of hash is required. Use -h for more information on the supported types."
                )
            return

        # check if more than one wordlist is provided
        if len(args.wordlists) > 1:
            cracked_password, matched_wordlist = crack_hash_multi_wordlists(
                args.digest, args.wordlists, args.type
            )
            (
                print(
                    f"Cracked 🥳 password: '{cracked_password}' found in \"{matched_wordlist}\" file"
                )
                if cracked_password
                else print(
                    "😞 Password not found in any of the wordlists. Consider using bigger wordlists or trying different dictionaries"
                )
            )
        else:  # only one wordlist is provided
            wordlist = read_wordlist(args.wordlists[0])
            cracked_password = crack_hash(args.digest, wordlist, args.type)
            (
                print(f"Cracked 🥳 password: '{cracked_password}'")
                if cracked_password
                else print(
                    "😞 Password not found in wordlist. Consider using a bigger wordlist or trying a different dictionary"
                )
            )
        return
    except Exception as e:
        print(f"-- 😩 Error: {e}")


if __name__ == "__main__":
    main()
