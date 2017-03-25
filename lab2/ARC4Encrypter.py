import sys
from Crypto.Cipher import ARC4

if len(sys.argv) >= 4:
    text_file = open(sys.argv[1], 'r+')
    key = sys.argv[2]
    cryptogram_file = open(sys.argv[3], 'r+')
    crypter = ARC4.new(key)
    if len(sys.argv) == 4:
        cryptogram_file.write(crypter.encrypt(text_file.read()))
    if len(sys.argv) == 5:
        encrypted_string = cryptogram_file.read()
        decrypted_string = crypter.decrypt(encrypted_string)
        text_file.write(decrypted_string)

