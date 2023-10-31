"""
Module for converting massive bitcoin private keys to Uncompressed WIF.
"""

import binascii
import hashlib
import base58
from common import process_file

def convert(hex_private_key):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF) for Uncompressed addresses.
    """
    with open('list-WIF.txt', 'a', encoding='utf-8') as file:
        extended_key = "80" + hex_private_key
        first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extended_key + second_sha256[:8]
        wif = base58.b58encode(binascii.unhexlify(final_key)).decode('ascii')
        file.write(f"{wif}\n")

# Call common.py to process the file
process_file("brute-pvks.txt", convert)

print("Conversion complete. Check your 'list-WIF.txt' file for the converted keys.")
print("_________________________________")
print("Donations for BTC: bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")
