from cryptography.fernet import Fernet
from cipher import Cipher
key = Fernet.generate_key()


original_data = "some text"

cryptor_object = Cipher(key)
encrypted_data = cryptor_object.encrypt(original_data)
print(encrypted_data)
decrypted_data = cryptor_object.decrypt(encrypted_data)
print(decrypted_data)
