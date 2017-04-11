import sys
from Crypto.PublicKey import RSA
from Crypto import Random


if (len(sys.argv) == 4):

    file_key = open(sys.argv[1], 'r')
    file_to_process = open(sys.argv[2], 'r')
    file_to_save = open(sys.argv[3], 'w')

    rsa_obj = RSA.importKey(file_key.read())

    random_number = Random.new().read

    data_encypted = rsa_obj.encrypt(file_to_process.read(), random_number)

    file_to_save.write(data_encypted[0])