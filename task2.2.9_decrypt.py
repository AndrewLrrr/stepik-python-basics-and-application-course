import simplecrypt

passwords = []

with open('task2.2.9/passwords.txt') as psw:
    passwords.extend(psw.read().strip().split('\n'))
print(passwords)

with open('task2.2.9/encrypted.bin', 'rb') as inp:
    cipher_text = inp.read()
    for password in passwords:
        try:
            plaintext = simplecrypt.decrypt(password, cipher_text)
            print(plaintext)
            print(plaintext.decode('utf8'))
        except simplecrypt.DecryptionException:
            print('Password ' + password + ' is not valid')

