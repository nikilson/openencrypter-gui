from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from os import getcwd, mkdir, path

def Decrypter(title, private_key, read_path, password):
   title = "/{}.bin".format(title)
   file_in = open(read_path + title, "rb")

   private_key = RSA.import_key(open(private_key).read(), passphrase = password)

   enc_session_key, nonce, tag, ciphertext = \
      [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

   # Decrypt the session key with the private RSA key
   cipher_rsa = PKCS1_OAEP.new(private_key)
   session_key = cipher_rsa.decrypt(enc_session_key)

   # Decrypt the data with the AES session key
   cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
   data = cipher_aes.decrypt_and_verify(ciphertext, tag)
   plain_text = (data.decode("utf-8"))
   return plain_text
if __name__ == '__main__':
   key_path = path.join(getcwd(), ".keys")
   users_path = path.join(getcwd(), ".users")
   private_key = key_path + "/private.key"
   title = "testtext"
   password = "password"
   plain_text = Decrypter(title, private_key, users_path, password)
   print(plain_text)
   