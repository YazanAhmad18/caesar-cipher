import nltk
import re
from nltk.corpus import words, names
nltk.download('names', quiet=True)
name_list = names.words()
nltk.download('words', quiet=True)
word_list = words.words()



def encrypt(encrypt_text, shifted):
    encrypted_txt = ""
    for i in encrypt_text:
        if i.isupper():  
            letter_POS = ord(i) - ord('A')
            POS_shifted = (letter_POS + shifted) % 26 + ord('A')
            new_letter = chr(POS_shifted)
            encrypted_txt = encrypted_txt + new_letter

        elif i.islower(): 
            letter_Pos = ord(i) - ord('a')
            POS_shifted = (letter_Pos + shifted) % 26 + ord('a')
            new_letter = chr(POS_shifted)
            encrypted_txt= encrypted_txt + new_letter

        elif i.isdigit():
            new_numb = (int(i) + shifted) % 10
            encrypted_txt = encrypted_txt+str(new_numb)

        else:
            encrypted_txt =encrypted_txt+ i
    return encrypted_txt

def decrypt(decrypt_ciphertext, shifted):

    decrypted_txt = ""
    for i in decrypt_ciphertext:

        if i.isupper():
            letter_POS = ord(i) - ord('A')
            Retrun_shifted_POS = (letter_POS - shifted) % 26 + ord('A')
            old_letter = chr(Retrun_shifted_POS)
            decrypted_txt =decrypted_txt+old_letter

        elif i.islower():
            letter_POS = ord(i) - ord('a')
            Retrun_shifted_POS = (letter_POS - shifted) % 26 + ord('a')
            old_letter = chr(Retrun_shifted_POS)
            decrypted_txt = decrypted_txt+old_letter
            
        elif i.isdigit():
            old_number = (int(i) - shifted) % 10
            decrypted_txt =decrypted_txt+ str(old_number)
        else:
            decrypted_txt =decrypted_txt+ i

    return decrypted_txt





def count_words(text):
    candidate_words = text.split()
    word_count = 0 

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
    
    return word_count

def crack( encrypted ):
    decrypt_word =''
    
    for key in range(26):
        expected = decrypt(encrypted, key)
        word_count = count_words(expected)
        percentage = int(word_count / len(expected.split()) * 100)
        if percentage > 50:
            decrypt_word = expected

    if not decrypt_word :
        decrypt_word = "the text does not fit 50 percent"

    return decrypt_word

        


if __name__=="__main__":
    encrypted_smaple = encrypt('It was the best of times, it was the worst of times.', 3)
    decrypted_smaple= decrypt(encrypted_smaple, 3)
    decrypted_smaple_without_the_key = crack(encrypted_smaple)
    print(encrypted_smaple)
    print(decrypted_smaple)
    print(decrypted_smaple_without_the_key)

