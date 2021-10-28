import json
from base64 import b64encode,b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes


#FUNCTION TO ENCRYPT THE DATA AND RETURNS RESULT , KEY
def encryption(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv':iv, 'ciphertext':cipher_text})
    return result,key

#FUNCTION TO DECRYPT THE DATA AND RETURNS RESULT
def decryption(data,key):
    try:
        b64 = json.loads(data)
        iv = b64decode(b64['iv'])
        cipher_text = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(cipher_text), AES.block_size)
        print("The decrypted data is: ", pt)
        return pt
    except ValueError or KeyError:
        print("Incorrect decryption")