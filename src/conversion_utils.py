"""
Module for converting batch bitcoin hexadecimal private key WIF.
"""

import binascii
import hashlib
from . import base58

def convert_hex_to_wif(hex_private_key, compressed=False):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF).
    """
    prefix = "80"
    suffix = "01" if compressed else ""
    extended_key = prefix + hex_private_key + suffix

    first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
    second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
    final_key = extended_key + second_sha256[:8]

    wif = base58.b58encode(binascii.unhexlify(final_key)).decode('ascii')
    return wif
