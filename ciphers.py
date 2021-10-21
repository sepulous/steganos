
class Morse:
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
        '-': '-....-', '_': '..--.-', '\"': '.-..-.', '$': '...-..-'
    }

    @staticmethod
    def encode(input: str) -> str:
        result = ''
        for char in input:
            if char == ' ':
                result += ' '
            else:
                result += Morse.MAP[char.upper()] + ' '
        return result

    @staticmethod
    def decode(input: str) -> str:
        result = ''
        groups = input.split(' ')
        for group in groups:
            found = False
            for letter, morse in zip(Morse.MAP.keys(), Morse.MAP.values()):
                if group == morse:
                    result += letter + ' '
                    found = True
            if not found:
                result += '? '
        return result


CIPHERS = {
    'morse': Morse
}
