# Mass Private keys To WIF
This tool converts multiple bitcoin private keys from either HEX format or WIF (Wallet Import Format) to their respective formats, handling thousands of keys at once. It supports both uncompressed and compressed WIF formats.
* Note: Use this tool only when offline.

## Requirements
- Python 3

## How To Use:
1) Download or clone this tool (git clone https://github.com/ELHARAKA/MassPrivatekeysToWIF.git) to your computer.
2) Navigate to the tool folder.
   - To convert from HEX to WIF, create a text file named "brute-pvks.txt" and paste all your private keys (in HEX format) into this file, then save.
   - To convert from WIF to HEX, create a text file named "wif.txt" and paste all your WIF private keys into this file, then save.
3)
    - To generate WIF for uncompressed addresses from HEX, execute `pvkmassconvert.py` by double-clicking on it or running `python3 pvkmassconvert.py` from the command line.
    - To generate WIF for compressed addresses from HEX, execute `pvkmassconvert_compressed.py` by double-clicking on it or running `python3 pvkmassconvert_compressed.py` from the command line.
    - To convert from WIF to HEX, execute `pvkwif2hex.py` by double-clicking on it or running `python3 pvkwif2hex.py` from the command line.
4) The tool will export all converted private keys to a new text file within the same folder. Check "list-WIF-compressed.txt" & "list-WIF-uncompressed.txt" for WIF keys and "list-hex.txt" for HEX keys.

## Donations
If this tool saved you time or helped in any way, consider making a donation to support the developer:
BTC Address: bc1qttzkk555p78dyq9l8g7syza6n94ppysv66dps0
