#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from Crypto.Cipher import AES
import random
import sys
import re
keybytes = [0] * 16
# learn how to read string in a file
# plaintext = "Hello, testing text for COMP3632"
# ciphertext = cipher.encrypt(plaintext)

pattern = "[a-zA-Z0-9 \"\!'(),-./?]+"
pattern = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \"\!'(),-./?'"
def contains(set):
    for c in set:
        if c not in pattern:
            return 0
    return 1


f = open("aestext", "rb", buffering=0)
if f.mode == "rb":
    contents = f.readline()
f.close()

for i in range(16):
    for j in range(256):
        for k in range(256):
            keybytes[13] = i
            keybytes[14] = j
            keybytes[15] = k

            key = bytes(bytearray(keybytes))
            cipher = AES.new(key, AES.MODE_ECB)
            decipher = cipher.decrypt(contents)

            try:
                test = decipher.decode()
            except UnicodeDecodeError:
                continue
            else:
                print "found"
                print test


            # if contains(decipher):
            #     print decipher
            #     f = open ("de_aestext", "w")
            #     f.write(decipher)
            #     f.close()
            #     sys.exit()
