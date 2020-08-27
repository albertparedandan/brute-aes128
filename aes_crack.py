from Crypto.Cipher import AES
from langdetect import detect
# import enchant
# dictionary = enchant.Dict("en_US") #shd we add brit too?

aesfile = open("aestext", "rb", buffering=0)
if aesfile.mode == "rb":
    aesbyte = aesfile.readline()
aesfile.close()

# create array for key
keybytes = [0] * 16

count = 0
# loop through every possible key combination
for m in range (16):
    keybytes[13] = m
    for k in range(256):
        keybytes[14] = k
        for l in range(256):
            keybytes[15] = l

            # decrypt the text
            key = bytes(bytearray(keybytes))
            cipher = AES.new(key, AES.MODE_ECB)
            plainbyte = cipher.decrypt(aesbyte)

            # convert text to string
            try:
                plaintext = plainbyte.decode()
            except UnicodeDecodeError:
                count += 1
                continue # move on if there are non ASCII characters
            else:
                # check if its an english sentence
                if (detect(plaintext) == 'en'):
                    f = open("de_aestext", "wb")
                    f.write(plaintext)
                    f.close()
                    exit
print count
