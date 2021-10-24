from ciphers.abstractcipher import AbstractCipher
from random import choice

class LeetSpeak(AbstractCipher):
    MAP = {
        'A': ['4', '@', '/\\', 'Д'],
        'B': ['8', 'ß', '|3', 'β'],
        'C': ['¢', '©', '(', '<'],
        'D': ['|)', '[)', '|>'],
        'E': ['3', '€', 'ε'],
        'F': ['ƒ', '|='],
        'G': ['&', '6', '[,', '{,'],
        'H': ['#', '|-|', '|~|', ':-:', '(-)', '1-1'],
        'I': ['|', ']['],
        'J': [',_|', ']', ';'],
        'K': ['|<', '|c', '|{'],
        'L': ['7', '£', '|_'],
        'M': ['/V\\', '[V]', '|\/|', '(v)', 'IVI'],
        'N': ['И', '|\|'],
        'O': ['0', 'Ø', '()'],
        'P': ['|*', '|°', '|o', '?'],
        'R': ['I2', 'Я', '®'],
        'S': ['5', '$', '§'],
        'T': ['7', '+', '†'],
        'U': ['v', 'μ', '(_)'],
        'V': ['\\/'],
        'W': ['VV', '\^/', '\|/', 'Ш'],
        'X': ['Ж', '×', '><'],
        'Y': ['Ч', '¥'],
    }

    @staticmethod
    def key_type() -> type:
        return None

    @staticmethod
    def encode(string: str, key=None) -> str:
        encoded = ''
        for char in string.upper():
            try:
                encoded += choice(LeetSpeak.MAP[char]) + ' '
            except KeyError:
                encoded += char
        return encoded

    @staticmethod
    def decode(string: str, key=None) -> str:
        decoded = ''
        for char in string.split(' '):
            matched = False
            for key in LeetSpeak.MAP:
                group = LeetSpeak.MAP[key]
                if char in group:
                    decoded += key
                    matched = True
                    break
            if not matched:
                decoded += char
            
        return decoded
