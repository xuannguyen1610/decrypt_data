from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64decode
'''from Data import get_data_from_api'''

def decrypt_aes(data, key):
    key = key.encode('utf-8')[:32]
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(b64decode(data)) + decryptor.finalize()

    return decrypted_data.decode('utf-8')

