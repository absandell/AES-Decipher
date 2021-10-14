import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.py3compat import is_string
from sys import getsizeof

with open("keygame.txt") as f:
    lines = f.readlines()

counter = 0
iv = k0 = k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = k10 = k11 = k12 = k13 = k14 = k15 = ''

for line in lines:
    if (counter == 0):
        iv = line.encode("utf-8")
        counter += 1
    elif (counter == 1):
        k0 = line.encode("utf-8")
        counter += 1
    elif (counter == 2):
        k1 = line.encode("utf-8")
        counter += 1
    elif (counter == 3):
        k2 = line.encode("utf-8")
        counter += 1
    elif (counter == 4):
        k3 = line.encode("utf-8")
        counter += 1
    elif (counter == 5):
        k4 = line.encode("utf-8")
        counter += 1
    elif (counter == 6):
        k5 = line.encode("utf-8")
        counter += 1
    elif (counter == 7):
        k6 = line.encode("utf-8")
        counter += 1
    elif (counter == 8):
        k7 = line.encode("utf-8")
        counter += 1
print(len(k0))
print(len(k1))
#try:
iv = b64decode(iv)
ct = b64decode(k0)
cipher = AES.new(k0, AES.MODE_CBC, iv)
data = unpad(cipher.decrypt(ct), AES.block_size)
print("The message was: ", data)
#except ValueError:
  #  print("Incorrect decryption")

#iv = b64decode(b64['iv'])
#ct = b64decode(b64['ciphertext'])
#cipher = AES.new(key, AES.MODE_CBC, iv)
#pt = unpad(cipher.decrypt(ct), AES.block_size)