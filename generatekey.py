from Crypto.PublicKey import RSA
from os import getcwd, mkdir, path
from encrypter import Encrypter
def Generate_RSA(secret_code, directory):
    print("\nEnter 1 >> Standard Security(2048)\nEnter 2 >> Higher Security(3072)\
        \nEnter 3 >> Extreme Security(4096)")
    key_size_select = input("\nSelect your number Default(3072) : ")
    try:
        key_size_select = int(key_size_select)
    except:
        key_size_select = 0
    if key_size_select == 1:
        key_size = 2048
    elif key_size_select == 2:
        key_size = 3072
    elif key_size_select == 3:
        key_size = 4096
    else:
        print("Default key 3072 is selected !!")
        key_size = 3072
    key = RSA.generate(key_size)

    private_key = key.export_key(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")
    key_path = path.join(directory, ".keys")
    mkdir(key_path)

    file_out = open(key_path + "/private.key", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open(key_path + "/public.key", "wb")
    file_out.write(public_key)
    file_out.close()

    public_key = key_path + "/public.key"
    Encrypter("validator", private_key.decode(), public_key, key_path)
    #validator_file.file