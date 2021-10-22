
from abc import ABC, abstractstaticmethod

class AbstractCipher(ABC):
    @abstractstaticmethod
    def encode(input):
        pass

    @abstractstaticmethod
    def decode(input):
        pass
