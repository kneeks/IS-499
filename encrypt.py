# -*- coding: utf-8 -*-
"""
Outputs two files depending on users choice.

Decrypt or Encrypt a file named encrypted.txt

"""

from Crypto.Cipher import AES

def main(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    file_out = open("encrypted.txt".encode("utf-8"), "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]


def main2(key):
    file_in = open("encrypted.txt", "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    F = open('decrypt.txt', 'a')
    F.write((data.decode()))
    F.close()


if __name__ == '__main__':
    ERROR = ('Sorry, you typed the wrong option. Please try again')
    #default file (uncomment the lines)
    #data = 'CUNY'.encode("utf-8")
    #key = 'nikofinalproject'.encode("utf-8")
    print ('welcome to my program ~Niko Vaccaro' '\n')
    input('press enter to begin!' '\n')
    A = (input('Encrypt or Decrypt: '))
    if A[0].lower() == 'e':
        #user file
        data = (input('Text to encrypt: ')).encode("utf-8")
        key = (input('Password to use (must be 16 chars): ')).encode("utf-8")
        main(data, key)
        print ('Thank you...')
    elif A[0].lower() == 'd':
        key = (input('Password to file (must be 16 chars): ')).encode("utf-8")
        main2(key)
        f = (open('decrypt.txt', 'r'))
        print (f.read())
        print('Thank you...')
    else:
        print (ERROR)


