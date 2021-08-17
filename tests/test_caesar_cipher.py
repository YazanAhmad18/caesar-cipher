from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import crack,encrypt,decrypt

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    word = 'perfect'
    key = 3
    actual = encrypt(word,3)
    expected = 'shuihfw'
    assert actual == expected

def test_decrypt():
    word = 'shuihfw'
    key = 3
    actual = decrypt(word,3)
    expected = 'perfect'
    assert actual == expected


def test_crack():
    word ='shuihfw'
    actual = crack(word)
    expected = 'perfect'
    assert actual == expected
