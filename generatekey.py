from Crypto.PublicKey import RSA
from os import getcwd, mkdir, path
from encrypter import Encrypter
def Generate_RSA(secret_code, directory):
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