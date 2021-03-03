import hashlib


print ('Escribe el texto que deseas cifrar:')
cadena = input()

print ('Escribe el algoritmo que desees utilizar de los siguientes:\n')

print ('blake2b\n')
print ('blake2s\n')
print ('md5\n')
print ('sha1\n')
print ('sha224\n')
print ('sha256\n')
print ('sha384\n')
print ('sha3_224\n')
print ('sha3_256\n')
print ('sha3_384\n')
print ('sha3_512\n')
print ('sha512\n')

algoritmo = input()

if algoritmo == "blake2b":
    c = hashlib.blake2b()
    c.update(cadena.encode('utf-8'))
if algoritmo == "blake2s":
    c = hashlib.blake2s()
    c.update(cadena.encode('utf-8'))
if algoritmo == "md5":
    c = hashlib.md5()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha1":
    c = hashlib.sha1()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha224":
    c = hashlib.sha224()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha256":
    c = hashlib.sha256()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha384":
    c = hashlib.sha384()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha3_224":
    c = hashlib.sha3_224()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha3_256":
    c = hashlib.sha3_256()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha3_384":
    c = hashlib.sha3_384()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha3_512":
    c = hashlib.sha3_512()
    c.update(cadena.encode('utf-8'))
if algoritmo == "sha512":
    c = hashlib.sha512()
    c.update(cadena.encode('utf-8'))

print ('Tu texto cifrado es:', (c.hexdigest()))
