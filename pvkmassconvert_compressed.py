"""
Module for converting massive bitcoin private keys to compressed WIF.
"""

import binascii
import hashlib
import base58

def convert(hex_private_key):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF) for compressed addresses.
    """
    with open('list-WIF.txt', 'a', encoding='utf-8') as file:
        extended_key = "80" + hex_private_key + "01"
        first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extended_key + second_sha256[:8]
        wif = base58.b58encode(binascii.unhexlify(final_key)).decode('ascii')
        print("Private Key on WIF Compressed format below")
        print(wif)
        file.write(f"{wif} \n")

with open("brute-pvks.txt", encoding='utf-8') as file_handle:
    for line in file_handle:
        print(str.strip(line))
        convert(str.strip(line))

print("__________________________________________________\n")
print("Developed by: Fahd El Haraka")
print("If this saved you time or helped, donations please for BTC Address:")
print("bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")
