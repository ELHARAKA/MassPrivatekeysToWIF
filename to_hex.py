"""
Module for transforming numerous bitcoin private keys from WIF format to HEX format.
"""

from src import base58

def wif_to_hex(wif_key):
    """
    Convert a WIF private key back to its hexadecimal representation.
    """
    with open('hex_output.txt', 'a', encoding='utf-8') as file:
        decoded = base58.b58decode(wif_key).hex()
        hex_key = decoded[2:-10]
        file.write(f"{hex_key}\n")

def process_file(file_path, conversion_function):
    """
    Process a file with a specified conversion function.
    """
    with open(file_path, encoding='utf-8') as file_handle:
        for line in file_handle:
            conversion_function(str.strip(line))

# Call common.py to process the file
process_file("wif_input.txt", wif_to_hex)

print("Conversion successful. Check your 'hex_output.txt'.")
print("_________________________________")
print("Donations for BTC: bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")
