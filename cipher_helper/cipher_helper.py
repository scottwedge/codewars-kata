#!/usr/bin/env python3

# The Vigenère cipher is a classic cipher originally developed by Italian cryptographer Giovan Battista Bellaso and published in 1553. It is named after a later French cryptographer Blaise de Vigenère, who had developed a stronger autokey cipher (a cipher that incorporates the message of the text into the key).
# 
# The cipher is easy to understand and implement, but survived three centuries of attempts to break it, earning it the nickname "le chiffre indéchiffrable" or "the indecipherable cipher."
# 
# From Wikipedia:
# 
#     The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.
# 
#     . . .
# 
#     In a Caesar cipher, each letter of the alphabet is shifted along some number of places; for example, in a Caesar cipher of shift 3, A would become D, B would become E, Y would become B and so on. The Vigenère cipher consists of several Caesar ciphers in sequence with different shift values.
# 
# Assume the key is repeated for the length of the text, character by character. Note that some implementations repeat the key over characters only if they are part of the alphabet -- this is not the case here.
# 
# The shift is derived by applying a Caesar shift to a character with the corresponding index of the key in the alphabet.
# 
# Visual representation:
# 
# "my secret code i want to secure"  // message
# "passwordpasswordpasswordpasswor"  // key
# 
# Write a class that, when given a key and an alphabet, can be used to encode and decode from the cipher.
# Example
# 
# var alphabet = 'abcdefghijklmnopqrstuvwxyz';
# var key = 'password';
# 
# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
# var c = new VigenèreCipher(key, alphabet);
# 
# c.encode('codewars'); // returns 'rovwsoiv'
# c.decode('laxxhsj');  // returns 'waffles'
# 
# Any character not in the alphabet must be left as is. For example (following from above):
# 
# c.encode('CODEWARS'); // returns 'CODEWARS'
# 
# 
# abc = "abcdefghijklmnopqrstuvwxyz"
# key = "password"
# c = VigenereCipher(key, abc)
# 
# test.assert_equals(c.encode('codewars'), 'rovwsoiv')
# test.assert_equals(c.decode('rovwsoiv'), 'codewars')
# 
# test.assert_equals(c.encode('waffles'), 'laxxhsj')
# test.assert_equals(c.decode('laxxhsj'), 'waffles')
# 
# test.assert_equals(c.encode('CODEWARS'), 'CODEWARS')
# test.assert_equals(c.decode('CODEWARS'), 'CODEWARS')

def test_encode_waffles():
    assert vc.encode("waffles") == "laxxhsj"

def test_encode_CODEWARS():
    assert vc.encode("CODEWARS") == "CODEWARS"

def test_decode_laxxhsj():
    assert vc.decode("laxxhsj") == "waffles"

def test_decode_CODEWARS():
    assert vc.decode("CODEWARS") == "CODEWARS"


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def encode(self, text):
        self.text = text
        result = ""
        for j in range(len(self.text)):
            if self.text[j] in self.alphabet:  # Ensure char is lowercase alphbet
                val = (self.alphabet.index(self.text[j]) + offset[j]) % len(self.alphabet)
                print(j, ":", val, list(self.alphabet)[val])
                result += self.alphabet[val]
            else:
                result += self.text[j]
        return result
    
    def decode(self, text):
        self.text = text
        result = ""
        for j in range(len(self.text)):
            if self.text[j] in self.alphabet:  # Ensure char is lowercase alphbet
                val = (self.alphabet.index(self.text[j]) - offset[j]) % len(self.alphabet)
                print(j, ":", val, list(self.alphabet)[val])
                result += self.alphabet[val]
            else:
                result += self.text[j]
        return result
    

    def wrap_key(self, key):
        self.key = key
        self.wrapped_key = self.key
        for j in range(len(self.alphabet)//len(self.key)):
            self.wrapped_key += self.key
        self.wrapped_key = self.wrapped_key[0:len(self.alphabet)]
        return self.wrapped_key

    def calc_offset(self, alphabet, wrapped_key):
        self.alphabet = alphabet
        self.wk = wrapped_key
        self.offset = []  # Initialize offset per position
        print("DEBUG____ self.alphabet= ", self.alphabet)  #DEBUG
        for j in range(len(self.alphabet)):
            key_offset = self.alphabet.index(self.wk[j]) 
#            self.offset.append(key_offset)
#            print(j, ":", key_offset)
            print(j, " of ", len(self.alphabet))
        return self.offset

text = "waffles"

a = "abcdefghijklmnopqrstuvwxyz"
a_list = list(a)
print("Alphabet= ", a)
print("a_list= ", a_list)
key = "password"
vc = VigenereCipher(a, key)
print("Key= ",vc.key)
wk = vc.wrap_key(key)
print("Wrapped key= ", wk)

offset = vc.calc_offset(a, wk)

result = vc.encode(text)
print("RESULT___ = ", result)

text2 = "laxxhsj"
result2 = vc.decode(text2)
print(result2)


key = "pizza"
text3 = 'psgvwjnw' 
#should equal 'pancakes'
vc2 = VigenereCipher(a, key)

result3 = vc2.encode(text3)

