plain_text=input('Enter plain Text: ')
plain_text=plain_text.lower()
cipher_text=''
enc_key=input('Enter Key: ')
enc_key=enc_key.lower()
keys='abcdefghijklmnopqrstuvwxyz'
plain_text2=''
while len(enc_key)<len(plain_text):
    enc_key+=enc_key
    if len(enc_key)>len(plain_text):
        enc_key=enc_key[:len(plain_text)]
print(enc_key)
for i,j in zip(plain_text,enc_key):
    c=(keys.index(i)+keys.index(j))%26
    cipher_text+=keys[c]
print('The encrypted message is:' +cipher_text)
for i,j in zip(cipher_text,enc_key):
    c=(keys.index(i)-keys.index(j)+26)%26
    plain_text2+=keys[c]
print('The decrypted message is:' + plain_text2)