import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.py3compat import is_string
from sys import getsizeof

lines = open("keygame.txt").read().split('\n')

counter = 0
iv = k0 = k1 = k2 = k3 = k4 = k5 = k6 = k7 = k8 = k9 = k10 = k11 = k12 = k13 = k14 = k15 = ''


for line in lines:
    if (counter == 0):
        iv = line
        counter += 1
    elif (counter == 1):
        k0 = str.encode(line)
        counter += 1
    elif (counter == 2):
        k1 = str.encode(line)
        counter += 1
    elif (counter == 3):
        k2 = str.encode(line)
        counter += 1
    elif (counter == 4):
        k3 = str.encode(line)
        counter += 1
    elif (counter == 5):
        k4 = str.encode(line)
        counter += 1
    elif (counter == 6):
        k5 = str.encode(line)
        counter += 1
    elif (counter == 7):
        k6 = str.encode(line)
        counter += 1
    elif (counter == 8):
        k7 = str.encode(line)
        counter += 1

print(k0)
for i in range(len(k0)):
    print(i+1, ": ", k0[i])

print(k1)
for i in range(len(k1)):
    print(i+1, ": ", k1[i])

print(iv)
for i in range(len(iv)):
    print(i+1, ": ", iv[i])
#try:
#iv = b64decode(iv)
#ct = b64decode(iv)

cipher = AES.new(k0, AES.MODE_CBC, iv)
data = unpad(cipher.decrypt(k0), AES.block_size)
print("The message was: ", data)
#except ValueError:
#  print("Incorrect decryption")

#iv = b64decode(b64['iv'])
#ct = b64decode(b64['ciphertext'])
#cipher = AES.new(key, AES.MODE_CBC, iv)
#pt = unpad(cipher.decrypt(ct), AES.block_size)