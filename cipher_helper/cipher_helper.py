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
    def __init__(self, alpha, key):
        self.key = key
        self.alpha = alpha
        print("DEBUG____ self.key= ", self.key)  # DEBUG
        print("DEBUG____ self.alpha= ", self.alpha)  # DEBUG
    
    def encode(self, text):
        self.text = text
        print("DEBUG____ self.text= ", self.text)  # DEBUG
        result = ""
        for j in range(len(self.text)):
            if self.text[j] in self.alpha:  # Ensure char is lowercase alphbet
                print("DEBUG____ self.text[j]= ", self.text[j])  # DEBUG
                print("DEBUG____ self.offset= ", self.offset)  # DEBUG
                print("DEBUG____ self.offset[j]= ", self.offset[j])  # DEBUG
                val = (self.alpha.index(self.text[j]) + self.offset[j]) % len(self.alpha)
                print(j, ":", val, list(self.alpha)[val])
                result += self.alpha[val]
            else:
                result += self.text[j]
        return result
    
    def decode(self, text):
        self.text = text
        result = ""
        for j in range(len(self.text)):
            if self.text[j] in self.alpha:  # Ensure char is lowercase alphbet
                val = (self.alpha.index(self.text[j]) - self.offset[j]) % len(self.alpha)
                print(j, ":", val, list(self.alpha)[val])
                result += self.alpha[val]
            else:
                result += self.text[j]
        return result
    

    def wrap_key(self, key):
        self.key = key
        self.wk = key
        for j in range(len(self.alpha)//len(self.key)):
            self.wk += self.key
        print("DEBUG1______ wrapped_key = ", self.wk)
        print("DEBUG_1_____ alphabet = ", self.alpha)
        self.wk = self.wk[0:len(self.alpha)]
        print("DEBUG2______ wrapped_key = ", self.wk)
#        return self.wk

#    def calc_offset(self, alpha, wk):
    def calc_offset(self):
#        self.alpha = alpha
#        self.wk = wk
        self.offset = []  # Initialize offset per position
        print("DEBUG____ self.alpha= ", self.alpha)  #DEBUG
        for j in range(len(self.alpha)):
            key_offset = self.alpha.index(self.wk[j]) 
            self.offset.append(key_offset)
#            print(j, ":", key_offset)
            print(j, " of ", len(self.alpha), "offset= ", key_offset)
#        return self.offset
        print(self.offset)


text = "waffles"

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_list = list(alpha)
print("Alpha= ", alpha)  # DEBUG
print("alpha_list= ", alpha_list)  # DEBUG

key = "password"

vc = VigenereCipher(alpha, key)  # create object

vc.wrap_key(key)

vc.calc_offset()

result = vc.encode(text)
print("RESULT1___ = ", result)  # DEBUG


text2 = "laxxhsj"
result2 = vc.decode(text2)
print("RESULT2____ = ", result2)  # DEBUG


# key = "pizza"
# text3 = 'psgvwjnw' 
# #should equal 'pancakes'
# vc2 = VigenereCipher(a, key)
# 
# result3 = vc2.encode(text3)
# 
