from ciphers.abstractcipher import AbstractCipher

class Morse(AbstractCipher):
    MAP = {
        'A': '.-',     'B': '-...',   'C': '-.-.',    'D': '-..',
        'E': '.',      'F': '..-.',   'G': '--.',     'H': '....',
        'I': '..',     'J': '.---',   'K': '-.-',     'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',     'P': '.--.',
        'Q': '--.-',   'R': '.-.',    'S': '...',     'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',     'X': '-..-',
        'Y': '-.--',   'Z': '--..',   '1': '.----',   '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',   '6': '-....',
        '7': '--...',  '8': '---..',  '9': '----.',   '0': '-----',
        '.': '.-.-.-', ',': '--..--', '?': '..--..',  '\'': '.----.',
        '!': '-.-.--', '(': '-.--.',  ')': '-.--.-',  '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-',   '+': '.-.-.',
        '-': '-....-', '_': '..--.-', '\"': '.-..-.', '$': '...-..-',
        ' ': ' ', '\n': '\n'
    }

    @staticmethod
    def takes_key() -> bool:
        return False

    @staticmethod
    def encode(input: str, key=None) -> str:
        encoded = []
        for char in input:
            if char == ' ':
                encoded.append(char)
            else:
                encoded.append(Morse.MAP[char.upper()])
        return ' '.join(encoded)

    @staticmethod
    def decode(input: str, key=None) -> str:
        decoded = []
        groups = input.split(' ') # Note: Each group represents a single character
        last_group = None
        for group in groups:
            found = False
            for letter, morse in zip(Morse.MAP.keys(), Morse.MAP.values()):
                if group == morse:
                    decoded.append(letter)
                    found = True
                    last_group = group
            if not found and group == '':
                if not last_group == '':
                    decoded.append(' ')
                    last_group = group
        return ''.join(decoded)
