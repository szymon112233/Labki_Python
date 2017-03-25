from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

if (len(sys.argv) == 6):
    input_file = open(sys.argv[1], 'rb')
    output_file = open(sys.argv[2], 'wb')
    mode = sys.argv[4]
    aes_mode = sys.argv[5]
    if(len(sys.argv[3]) == 16 or len(sys.argv[3]) == 24 or len(sys.argv[3]) == 32):
        iv = get_random_bytes(16)
        if (aes_mode == "-cbc"):
            aes = AES.new(sys.argv[3],AES.MODE_CBC, iv)
        elif (aes_mode == "-ecb"):
            aes = AES.new(sys.argv[3], AES.MODE_ECB, iv)

        header = input_file.read(54)
        input_bytes = input_file.read()
        if (len(input_bytes) % 16 != 0):
            print len(input_bytes) % 16
        output_bytes = header
        if (mode == "-encrypt"):
            output_bytes += aes.encrypt(input_bytes)
        elif (mode == "-decrypt"):
            output_bytes += aes.decrypt(input_bytes)
        output_file.write(output_bytes)
    else:
        print "Key should be 16, 24 or 32 bytes long!"
