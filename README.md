# Mass Private keys To WIF
This tool converts multiple bitcoin private keys from hexadecimal format to WIF (Wallet Import Format) for importing into any wallet, or for mass importing into Electrum Wallet, handling thousands of keys at once.
* Note: Use this tool only when offline.

## Requirements
- Python 3

## How To Use:
1) Download or clone this tool (git clone https://github.com/ELHARAKA/MassPrivatekeysToWIF.git) to your computer.
2) Navigate to the tool folder, create a text file named "brute-pvks.txt" and paste all your private keys (in hexadecimal format) into this file, then save.
3) 
    - To generate WIF for uncompressed addresses, execute `pvkmassconvert.py` by double-clicking on it or running `python3 pvkmassconvert.py` from the command line.
    - To generate WIF for compressed addresses, execute `pvkmassconvert_compressed.py` by double-clicking on it or running `python3 pvkmassconvert_compressed.py` from the command line.
4) The tool will export all private keys in WIF format to a new text file named "list-WIF.txt" within the same folder.

## Donations
If this tool saved you time or helped in any way, consider making a donation to support the developer:
BTC Address: bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0
