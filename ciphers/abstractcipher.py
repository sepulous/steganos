
from abc import ABC, abstractstaticmethod

class AbstractCipher(ABC):
    @abstractstaticmethod
    def takes_key() -> bool:
        pass

    @abstractstaticmethod
    def encode(input, key=None):
        pass

    @abstractstaticmethod
    def decode(input, key=None):
        pass
