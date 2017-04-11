import sys
from Crypto.PublicKey import RSA



if (len(sys.argv) == 4):

    file_key = open(sys.argv[1], 'r')
    file_to_proces = open(sys.argv[2], 'r')
    file_to_save = open(sys.argv[3], 'w')

    rsa_obj = RSA.importKey(file_key.read())

    data_encypted = rsa_obj.decrypt(file_to_proces.read())

    file_to_save.write(data_encypted)