import base64
from Crypto.Cipher import AES

def xor_strings(a,b):
    return "".join([chr(ord(x)^ord(y)) for x,y in zip(a,b)])

lines = open("keygame.txt", 'r')
keys = lines.read().split("\n")
lines.close()

key0 = keys[0]
cipher_text = key0.encode("utf-8")

key9 = keys[9]
g = "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
print (len(key9))

print(len(g))
key9 = xor_strings(key9[7:], g)
keys[9] = 'KEY009-'+key9
print(keys[9])

iv = b"\xb5\xcdt\xe0\x91\xdb8V\x10\xbf\xab;'\xd8\xe9\x8a"
decrypt_cipher = AES.new(cipher_text, AES.MODE_CBC, iv)

for k in keys[1:]:
    if k != "":
        cipher_text += base64.b64decode(k[7:])

plain_text = decrypt_cipher.decrypt(cipher_text)

print(plain_text.decode())