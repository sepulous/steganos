from ciphers.abstractcipher import AbstractCipher
from ciphers.caesar import Caesar

class Vigenere(AbstractCipher):
    @staticmethod
    def key_type() -> type:
        return str

    @staticmethod
    def encode(string: str, code: str) -> str:
        print(code)
        if not 0 < len(code) <= len(string):
            raise Exception('Invalid code length.')

        code_index = 0
        upper_bound = len(code) - 1
        encoded = ''
        for char in string:
            shift = Caesar.key_type()(code[code_index])
            encoded += Caesar.encode(char, shift)
            if code_index == upper_bound:
                code_index = 0
            else:
                code_index += 1

        return encoded

    @staticmethod
    def decode(string: str, code: str) -> str:
        if not 0 < len(code) <= len(string):
            raise Exception('Invalid code length.')

        code_index = 0
        upper_bound = len(code) - 1
        decoded = ''
        for char in string:
            shift = Caesar.key_type()(code[code_index])
            decoded += Caesar.decode(char, shift)
            if code_index == upper_bound:
                code_index = 0
            else:
                code_index += 1

        return decoded
