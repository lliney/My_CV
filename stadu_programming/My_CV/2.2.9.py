from simplecrypt import encrypt, decrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt","rb") as pas:
    passwords=pas.read()
keys=[str(k) for k in passwords.split()]
for i in keys:
    i=i[2:]
    i=i[:-1]
    print(i)
    try:
       plaintext = decrypt(i, encrypted).decode("utf-8")
       print("Наша фраза - ",plaintext)
       break
    except:
        print('Неудачная попытка')