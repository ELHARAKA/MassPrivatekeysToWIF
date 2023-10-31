"""
Module for converting massive bitcoin private keys to compressed WIF.
"""

from src.conversion_utils import convert_hex_to_wif
from src.common import process_file

def convert(hex_private_key):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF) for Uncompressed addresses.
    """
    wif = convert_hex_to_wif(hex_private_key, compressed=True)
    with open('list-WIF-compressed.txt', 'a', encoding='utf-8') as file:
        file.write(f"{wif}\n")

# Call common.py to process the file
process_file("brute-pvks.txt", convert)

print("Conversion successful. Check your 'list-WIF-compressed.txt' file for the converted keys.")
print("__________________________________________________")
print("Developed by: Fahd El Haraka")
print("If this saved you time or helped, donations please for BTC Address:")
print("bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")
