"""
Module for converting batch bitcoin private keys to WIF (Compressed & Uncompressed).
"""

import binascii
from src.conversion_utils import convert_hex_to_wif
from src.common import process_file

def is_valid_hex_key(hex_key):
    """
    Validate if the given string is a valid hexadecimal.
    """
    try:
        int(hex_key, 16)
        return True
    except ValueError:
        return False

def convert_compressed(hex_private_key):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF) for compressed addresses.
    """
    wif = convert_hex_to_wif(hex_private_key, compressed=True)
    with open('compressed_output.txt', 'a', encoding='utf-8') as file:
        file.write(f"{wif}\n")

def convert_uncompressed(hex_private_key):
    """
    Convert a hexadecimal private key to Wallet Import Format (WIF) for uncompressed addresses.
    """
    wif = convert_hex_to_wif(hex_private_key, compressed=False)
    with open('uncompressed_output.txt', 'a', encoding='utf-8') as file:
        file.write(f"{wif}\n")

def process_both_conversions(hex_private_key):
    """
    Process both compressed and uncompressed WIF conversions for a given HEX private key.

    Args:
        hex_private_key (str): The hexadecimal private key to be converted.
    """
    if is_valid_hex_key(hex_private_key):
        convert_compressed(hex_private_key)
        convert_uncompressed(hex_private_key)
    else:
        print(f"Invalid hexadecimal key: {hex_private_key}")

# Call common.py to process the file with both conversion functions
process_file("hex_input.txt", process_both_conversions)

print("Conversion process completed. Check 'compressed_output.txt' and 'uncompressed_output.txt' files for the converted keys.")
print("__________________________________________________")
print("Developed by: Fahd El Haraka")
print("If this saved you time or helped, donations please for BTC Address:")
print("bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")
