<p align="center">
  <img src="https://pub-4921d2344b4d4baab627f5944ec5b7b0.r2.dev/Archive/assets/MassPrivatekeysToWIF.png" alt="MassPrivatekeysToWIF" width="350">
</p>

# Mass Private keys To WIF
This tool converts multiple bitcoin private keys from either HEX format or WIF (Wallet Import Format) to their respective formats, handling thousands of keys at once. It supports both uncompressed and compressed WIF formats.
* Note: Use this tool only when offline.

## Requirements
- Python 3

## How To Use:
1) Download or clone this tool (git clone https://github.com/ELHARAKA/MassPrivatekeysToWIF.git) to your computer.
2) Navigate to the tool folder.
   - To convert from HEX to WIF, create a text file named "hex_input.txt" and paste all your (HEX format) private keys.
   - To convert from WIF to HEX, create a text file named "wif_input.txt" and paste all your (WIF format) private keys.
3)
    - To generate WIF (Compressed) run `python3 WIF_compressed.py`
    - To generate WIF (Uncompressed) run `python3 WIF_uncompressed.py`
    - To generate HEX from WIF, run `python3 WiftoHex.py`

4) The tool will export all converted private keys to a new text file(s) within the same directory. Check `compressed_output.txt` or `uncompressed_output.txt` for WIF keys OR `hex_output.txt` for HEX keys.

## Donations
If this tool saved you time or helped in any way, consider making a donation to support the developer:
* BTC Address: bc1q6zf7gxr7xqktv7gqdt7k9nawq8mu0xs99xrzrf
