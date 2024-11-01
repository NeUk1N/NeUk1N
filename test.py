import tink
from tink import aead
import os


def encrypt(file_path):
    file_path = input ("Введите путь до файла:")

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    associated_data = b''

    aead.register()

    keyset_handle = tink.new_keyset_handle(aead.aead_key_templates.AES256_GCM)
    aead_primitive = keyset_handle.primitive(aead.Aead)

    ciphertext = aead_primitive.encrypt(plaintext, associated_data)

    with open(file_path + '.enc', 'wb') as file:
        file.write(ciphertext)
    os.remove(file_path)

def deencrypt(file_path):
    
    pass
choice = int(input("Что вы хотите сделать?\n 1. Зашифровать файл\n 2. Расшифровать файл?\n"))

if choice == 1:
    encrypt()

os.mkdir("Папка с файлами", exist_ok=True)
os.mkdir("Папка с файлами/Зашифрованные файлы")