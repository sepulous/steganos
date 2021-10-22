import argparse
from pathlib import Path
from ciphers.ciphers import CIPHERS
from ciphers.abstractcipher import AbstractCipher

def is_file(string: str) -> bool:
    string = string.strip()
    return string.find(' ') == -1 and string.find('.') > 0

def file_exists(filename: str) -> bool:
    return Path(filename).is_file()

def main():
    parser = argparse.ArgumentParser()
    cipher_group = parser.add_mutually_exclusive_group()
    ciphers = list(CIPHERS.keys())
    cipher_group.add_argument('--encode', type=str, nargs='?', choices=ciphers, help='Encode using specified cipher',)
    cipher_group.add_argument('--decode', type=str, nargs='?', choices=ciphers, help='Decode using specified cipher',)
    parser.add_argument('-k', '--key', type=any)
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-o', '--output', type=str, required=False)
    args = vars(parser.parse_args())

    if args['encode']:
        cipher: AbstractCipher = CIPHERS[args['encode']]
    else:
        cipher: AbstractCipher = CIPHERS[args['decode']]

    if cipher.takes_key():
        if not args['key']:
            raise Exception('Key must be provided for this technique.')

    source = args['input']
    if is_file(source):
        if file_exists(source):
            with open(source, 'r') as file:
                input = file.read()
        else:
            print(f'Input file "{source}" does not exist.')
            return
    else:
        input = source

    if args['encode']:
        if cipher.takes_key():
            key = args['key']
            output = cipher.encode(input, key)
        else:
            output = cipher.encode(input)
    else:
        if cipher.takes_key():
            key = args['key']
            output = cipher.decode(input, key)
        else:
            output = cipher.decode(input)

    destination = args['output']
    if destination:
        if is_file(destination):
            with open(destination, 'w') as file:
                file.write(output)
        else:
            print(f'Invalid output destination: "{destination}"')
    else:
        print(output)

if __name__ == "__main__":
    main()
