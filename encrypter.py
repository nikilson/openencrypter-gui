from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from os import getcwd, mkdir, path
from decrypt import Decrypter

def Encrypter(title, plain_text, public_key, write_path):
	plain_text = plain_text.encode("utf-8")
	title = "/{}.bin".format(title)
	try:
		file_out = open(write_path + title, "wb")
	except:
		mkdir(write_path)
		file_out = open(write_path + title, "wb")
	session_key = get_random_bytes(16)

	public_key = RSA.import_key(open(public_key).read())
	# Encrypt the session key with the public RSA key
	cipher_rsa = PKCS1_OAEP.new(public_key)
	enc_session_key = cipher_rsa.encrypt(session_key)

	# Encrypt the data with the AES session key
	cipher_aes = AES.new(session_key, AES.MODE_EAX)
	ciphertext, tag = cipher_aes.encrypt_and_digest(plain_text)
	[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
	file_out.close()
if __name__ == '__main__':
	data = "This is Rinaldo Nikilson."
	key_path = path.join(getcwd(), ".keys")
	public_key = key_path + "/public.key"
	users_path = path.join(getcwd(), ".users")
	title = "testtext"
	Encrypter(title, data, public_key, users_path)