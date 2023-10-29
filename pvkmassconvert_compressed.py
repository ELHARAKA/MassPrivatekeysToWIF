import binascii
import hashlib
import base58

def convert(hex_key):
    """Converts a hexadecimal private key to compressed Wallet Import Format (WIF)."""
    with open('list-WIF.txt', 'a', encoding='utf-8') as arq:
        extended_key = "80" + hex_key + "01"
        first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extended_key + second_sha256[:8]
        wif = base58.b58encode(binascii.unhexlify(final_key)).decode('ascii')
        print("Private Key on WIF Compressed format below")
        print(wif)
        arq.write(f"{wif} \n")

def main():
    """Main function to read input file and convert keys."""
    with open("brute-pvks.txt", encoding='utf-8') as file:
        for line in file:
            print(str.strip(line))
            convert(str.strip(line))
    print("__________________________________________________\n")
    print("Developed by: Fahd El Haraka")
    print("If this saved you time or helped, evena small donation to dev would be appreciated.")
    print("BTC Address: bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")

if __name__ == "__main__":
    main()
