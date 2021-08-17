from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import crack,encrypt,decrypt

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    word = 'perfect'
    key = 5
    actual = encrypt(word,5)
    expected = 'ujwkjhy'
    assert actual == expected

def test_decrypt():
    word = 'ujwkjhy'
    key = 5
    actual = decrypt(word,5)
    expected = 'perfect'
    assert actual == expected


def test_crack():
    word ='ujwkjhy'
    actual = crack(word)
    expected = 'perfect'
    assert actual == expected
