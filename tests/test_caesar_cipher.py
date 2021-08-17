from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import crack,encrypt,decrypt

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    word = 'perfect'
    key = 3
    actual = encrypt(word,key)
    expected = 'shuihfw'
    assert actual == expected

def test_decrypt():
    word = 'shuihfw'
    key = 3
    actual = decrypt(word,key)
    expected = 'perfect'
    assert actual == expected


def test_crack1():
    actual = crack('Lw zdv wkh ehvw ri wlphv')
    expected = 'It was the best of times'
    assert actual == expected


def test_encrypt1():
    plain_text = "My Name is yazab ahmad. $ - % _ @ * # ^ underTest"
    key = 3
    actual = encrypt( plain_text, key )
    expected = "Pb Qdph lv bdcde dkpdg. $ - % _ @ * # ^ xqghuWhvw"
    assert actual == expected


def test_decrypt1():
    encrypted_text = "Pb Qdph lv bdcde dkpdg. $ - % _ @ * # ^ xqghuWhvw"
    key = 3
    actual = decrypt( encrypted_text, key )
    expected = "My Name is yazab ahmad. $ - % _ @ * # ^ underTest"
    assert actual == expected


def test_crack():
    actual = crack("Lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv.")
    expected = "It was the best of times, it was the worst of times."
    assert actual == expected


def test_encrypt4():
    word = 'perfect22'
    key = 3
    actual = encrypt(word,key)
    expected = 'shuihfw55'
    assert actual == expected

def test_decrypt4():
    word = 'shuihfw55'
    key = 3
    actual = decrypt(word,key)
    expected = 'perfect22'
    assert actual == expected



def test_crack6():
    actual = crack("lw zdv vxqqb")
    expected = "it was sunny"
    assert actual == expected


def test_crack7():
    actual = crack( "My Name is yazan ahmad and my age 22. $ - % _ @ * # ^ Test" )
    expected = "the text does not fit 50 percent"
    assert actual == expected