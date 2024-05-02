<p align="center">
  <img src="https://pub-4921d2344b4d4baab627f5944ec5b7b0.r2.dev/Archive/assets/MassPrivatekeysToWIF.png" alt="MassPrivatekeysToWIF" width="350">
</p>

# Mass Private keys To WIF
This tool converts multiple bitcoin private keys from either HEX format or WIF (Wallet Import Format) to their respective formats, handling thousands of keys at once. It supports both uncompressed and compressed WIF formats.
* Note: Use this tool only when offline.

## Requirements
- Python 3

## How To Use:
1) Download or clone this tool (git clone https://github.com/ELHARAKA/MassPrivatekeysToWIF.git)

2) Navigate to the tool folder.
   - For HEX to WIF conversion, create `hex_input.txt` and insert HEX-format keys.
   - For WIF to HEX conversion, create `wif_input.txt` and insert WIF-format keys.

3) Run the tool:
    - Generate WIF (Compressed & Uncompressed): `python3 toWIF.py`
    - Generate HEX from WIF: `python3 toHEX.py`

4) Output files:
    - WIF keys are in `compressed_output.txt` and `uncompressed_output.txt`.
    - HEX keys are in `hex_output.txt`.

## Donations
If this tool saved you time or helped in any way, consider making a donation to support the developer:
* BTC Address: bc1q6zf7gxr7xqktv7gqdt7k9nawq8mu0xs99xrzrf
