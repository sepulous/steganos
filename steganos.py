import argparse
from pathlib import Path
from ciphers.ciphers import CIPHERS

def is_file(string: str) -> bool:
    string = string.strip()
    return string.find(' ') == -1 and string.find('.') > 0

def file_exists(filename: str) -> bool:
    return Path(filename).is_file()

def main():
    parser = argparse.ArgumentParser()
    cipher_group = parser.add_mutually_exclusive_group()
    ciphers = list(CIPHERS.keys())
    cipher_group.add_argument('--encode', help='Encode using specified cipher', type=str, nargs='?', choices=ciphers)
    cipher_group.add_argument('--decode', help='Decode using specified cipher', type=str, nargs='?', choices=ciphers)
    parser.add_argument('-i', '--input', type=str, required=True)
    parser.add_argument('-o', '--output', type=str, required=False)
    args = vars(parser.parse_args())

    # Map cipher string to cipher class
    if args['encode']:
        cipher = CIPHERS[args['encode']]
    else:
        cipher = CIPHERS[args['decode']]

    # Set up input
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

    # Encode/decode
    if args['encode']:
        output = cipher.encode(input)
    else:
        output = cipher.decode(input)

    # Write output to file or terminal
    destination = args['output']
    if not destination:
        print(output)
    else:
        if is_file(destination):
            with open(destination, 'w') as file:
                file.write(output)
        else:
            print(f'Invalid output destination: "{destination}"')

if __name__ == "__main__":
    main()
