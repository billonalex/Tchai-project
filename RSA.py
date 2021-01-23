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
import sqlite3
from sqlite3 import Error
import time
from datetime import datetime
import hashlib

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

def encrypt(message, priv_key):
    #RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.encrypt(message)

def decrypt_public_key(encoded_encrypted_msg, public_key):
    encryptor = RSA.new(public_key)
    return encryptor.decrypt(encoded_encrypted_msg)
    #return decoded_decrypted_msg

def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()

def write_key_in_db(db_path, personne):
    conn = None

    try:
        key = RSA.generate(2048)
        pub_key = key.publickey()
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        query = "UPDATE public_key SET rsa_pub = \"" + str(pub_key.exportKey('PEM')) + "\" WHERE personne=" + str(personne)
        cur.execute(query)
        priv_file = open("private_key/" + str(personne) + ".txt", "w")

        priv_file.write(str(key.exportKey('PEM')))

        priv_file.close()
        conn.commit()


    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
        print("Done !")

#write_key_in_db(1)
#write_key_in_db(2)
#write_key_in_db(3)

message = b"Hello world"
print(message)
privat = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAt6BV8+IBIJsyNWXfk6FpJE6MD/uZPbbbpGCHEGr8DIGQjPT4\nrQE0XclEVNEfZmTgpBSipnznMBo/HLLMdxiz97RTx8ttYItd6I6vIE8tdSKits0P\nPNoOY15jXYpFC5jhGQLviQ1fD/nz5luS/KdlGcHQiA0GL9vtpGj70Y99Jqh1jWKe\nuaEMb0t2at4Y1hCszFKm7OrfimQcaZ7Cm2LB/kTxP551hxgl6X7ZdJGXUtzuRRgG\nbKX7WB3HO9rMG7oA1qWjrVDnpCLw4ugP0dKh9IAUAs2CXpvZBn4Qsp4X3LABPQPx\nPmotzXKu2ex1w6tQ8Lg+KV5/SmgXFmBNbtLfXwIDAQABAoIBACcCUlAxsoCdR7DN\nWA5SS3ZRk3KvxfG033tPoFHOEIaNnco8HnoOV/QWlkQYev2zL3/b/GO3BBwVb1Pm\n7gXdAxp7vhKjNjS81rHZYf3QpD0OoxeHf5WzUzwr6JsODTX1/9fi5kUsyIWp2XUV\n/idbXmB26piEf8x6AcWcIeb2fyVPZsetDtPMv+VjsRXxI7tnlw5Nt2HiZzIog7Ne\nuVm/h6yYUrWsMcNndTTLh0YVjvd/MtOON8cykZTznRGe7Cz/gQWOsqS0LzneUbU6\nlLfE+icaRiG2BI6fxZQMBK1VxQEkNwmrK9fu44EZyLH3dzJ6aRpUKi2vqTcnGfum\nHLBaNvECgYEAxXS5d3+B7v+L9vft2h9pEyaexmyuEHyWMkjxB9ie0Y47L7sC9uGA\n4IJfzrLffZDvAYk57PZFBdyuSUOAwsUHq6TjPmD/Oamjp6S9zDgsdQHSKG89jSmy\nl0UBasbR9tQ/fx4iR2gLWk3XCt1IBwgW1/i9P3/LzsFgpRn4PK3C2a8CgYEA7hHq\nX6bWE4OPF9xLcZv6Sh01C7WvTA9rKGrdSOWOhmKrokcYAcHSIvxnsu+TWxP/vH1U\ns7Br9W036AGsoLAJxjGSSlD3Dt7XcY559NvEWdSUk/N4Aytcq+anzKqPO4pJucp6\noPtcnu3FedQ0iqVgBUw1a8IYf0wF0MJ+Sit2sVECgYBZVQ+7wpI0YKUgHNcdQey1\n31kiCHVPvC3vnhR+KkDgKesZExCqRSebayCRUVfPZUzccwsj698aYdbwCnwsohtw\nSm8M/7E4k0kZRW0hAaELZsF/zaQZQ24rBes4Na80bp4zkpyLlcTdHC5YGfjGRaCg\nIUbtfZHlfpOM3ozyVuK6vQKBgQCfuNNWwzcDNpONPZY8LZqZmMjbB1UJoZqSLkgy\nPRkHHjHqmOoJW8EhCdiE22kwhNVh33Axch6sNU95z43C7PhRyTZNt85ZYraGkEFQ\nPxWX8yCPtpwA/FmbVw+jJ5cbKidWh/sIADxewEVp/C4YCuXGCCAbIMiQty97pNFX\n75sdUQKBgCWES0g0HiToyWstT8p22A/UrKAqWTt9329UHyTNqci/1KtlMcnNvNTV\n7RdoLnbZ1uf0ukDoUthMI7Oy0aXvE1DFw4VOZWDQTXY454dIs85VlB6UV/hG8qcp\nymzDrzL5j3cTOq5lhxvDdDlM6f8cChuKdC3DESI6krLCnHJusXHo\n-----END RSA PRIVATE KEY-----'

key = RSA.importKey(privat)

encoded = encrypt(message, key)

print(encoded)

#decoded = decrypt_public_key(encoded, public)

#print(decoded)
