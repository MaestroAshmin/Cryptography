def caesar( ):
    plain_text = input('Enter plain text: ')
    plain_text=plain_text.lower()
    cipher_text = ''
    plain_text2=''
    keys= 'abcdefghijklmnopqrstuvwxyz'
    key= int(input('Enter Key: '))
    for l in plain_text:
        try:
             c = (keys.index(l) + key) % 26
             cipher_text+= keys[c]
        except ValueError:
            cipher_text += ' '
    print('The encrypted message is :' + cipher_text)
    for l in cipher_text:
        try:
            c = (keys.index(l)-key) % 26
            plain_text2 += keys[c]
        except ValueError:
            plain_text2 += ' '
    print('The decrypted message is:' + plain_text2)

caesar()