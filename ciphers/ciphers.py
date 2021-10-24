from ciphers.morse import Morse
from ciphers.caesar import Caesar
from ciphers.rot13 import Rot13
from ciphers.vigenere import Vigenere
from ciphers.leetspeak import LeetSpeak

CIPHERS = {
    'morse': Morse,
    'caesar': Caesar,
    'rot13': Rot13,
    'vigenere': Vigenere,
    'leetspeak': LeetSpeak
}
