from ciphers.abstractcipher import AbstractCipher
from ciphers.caesar import Caesar

class Rot13(AbstractCipher):
    @staticmethod
    def takes_key() -> bool:
        return False

    @staticmethod
    def encode(string: str, key=None) -> str:
        return Caesar.encode(string, 13)

    @staticmethod
    def decode(string: str, key=None) -> str:
        return Caesar.decode(string, 13)
