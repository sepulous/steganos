from ciphers.abstractcipher import AbstractCipher
from string import ascii_letters

class Caesar(AbstractCipher):
    @staticmethod
    def key_type() -> type:
        return int

    @staticmethod
    def encode(input: str, shift: int):
        encoded = ''
        for char in input:
            if char not in ascii_letters:
                encoded += char
                continue

            new_val = ord(char) + shift
            lower, upper = (65, 90) if 65 <= ord(char) <= 90 else (97, 122)
            if new_val > upper:
                slack = new_val % upper
                encoded += chr(lower + slack)
            else:
                encoded += chr(new_val)

        return encoded

    @staticmethod
    def decode(input: str, shift: int):
        decoded = ''
        for char in input:
            if char not in ascii_letters:
                decoded += char
                continue

            new_val = ord(char) - shift
            lower, upper = (65, 90) if 65 <= ord(char) <= 90 else (97, 122)
            if new_val < lower:
                slack = lower - new_val
                decoded += chr(upper - slack)
            else:
                decoded += chr(new_val)

        return decoded
