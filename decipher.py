import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.py3compat import is_string
from sys import getsizeof

iv = 'b\"\xb5\xcdt\xe0\x91\xdb8V\x10\xbf\xab;\'\xd8\xe9\x8a\"'
key = 'KEY000-1234567890123456789012=='
print(getsizeof(iv))
print(getsizeof(key))

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
data = unpad(cipher.decrypt(key), AES.block_size)