import binascii, hashlib, base58, sys

def convert(z):
    with open('list-WIF.txt', 'a') as arq:  # Updated line
        private_key_static = z
        extended_key = "80" + private_key_static + "01"
        first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
        second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
        final_key = extended_key + second_sha256[:8]
        WIF = base58.b58encode(binascii.unhexlify(final_key)).decode('ascii')  # Updated line
        print("Private Key on WIF Compressed format below")
        print(WIF)
        arq.write(f"{WIF} \n")  # Updated line

with open("brute-pvks.txt") as file:
    for line in file:
        print(str.strip(line))  # Updated line
        convert(str.strip(line))

print("__________________________________________________\n")
print("Developed by: Fahd El Haraka")
print("If this saved you time or helped, donations please for BTC Address:")
print("bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0")
