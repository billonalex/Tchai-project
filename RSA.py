# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 09:43:48 2020

@author: Alexandre
"""

from uuid import uuid4
import os
import binascii
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from Crypto.PublicKey import RSA
import base64

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey() 
    private_key = new_key.exportKey() 
    return private_key, public_key

def encrypt(message, pub_key):
    #RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)

def decrypt_public_key(encoded_encrypted_msg, public_key):
    encryptor = RSA.new(public_key)
    return encryptor.decrypt(encoded_encrypted_msg)
    #return decoded_decrypted_msg

def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


priv, pub = generate_RSA()
#print(priv)
#print(pub)


privat = RSA.importKey(priv)
public = RSA.importKey(pub)
#print(privat)


message = b"Hello world"

encoded = encrypt(message, privat)

print(encoded)

decoded = decrypt_public_key(encoded, public)

print(decoded)

#print(generate_key())
#print(uuid4())
