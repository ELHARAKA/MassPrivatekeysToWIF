'''Base58 encoding

Implementations of Base58 and Base58Check encodings that are compatible
with the bitcoin network.
'''

import sys
import argparse
from hashlib import sha256

__version__ = '0.2.5'

ALPHABET = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def bseq(s):
    '''Convert sequence to bytes.'''
    return bytes(s)


def b58encode_int(i, default_one=True):
    '''Encode an integer using Base58.'''
    if not i and default_one:
        return ALPHABET[0:1]
    string = b""
    while i:
        i, idx = divmod(i, 58)
        string = ALPHABET[idx:idx + 1] + string
    return string


def b58encode(v):
    '''Encode a string using Base58.'''
    if isinstance(v, str):
        v = v.encode('ascii')

    n_pad = len(v)
    v = v.lstrip(b'\0')
    n_pad -= len(v)

    p, acc = 1, 0
    for c in v[::-1]:
        acc += p * c
        p = p << 8

    result = b58encode_int(acc, default_one=False)

    return ALPHABET[0:1] * n_pad + result


def b58decode_int(v):
    '''Decode a Base58 encoded string as an integer.'''
    if isinstance(v, str):
        v = v.encode('ascii')

    decimal = 0
    for char in v:
        decimal = decimal * 58 + ALPHABET.index(char)
    return decimal


def b58decode(v):
    '''Decode a Base58 encoded string.'''
    if isinstance(v, str):
        v = v.encode('ascii')

    orig_len = len(v)
    v = v.lstrip(ALPHABET[0:1])
    new_len = len(v)

    acc = b58decode_int(v)

    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)

    return b'\0' * (orig_len - new_len) + bytes(reversed(result))


def b58encode_check(v):
    '''Encode a string using Base58 with a 4 character checksum.'''
    if isinstance(v, str):
        v = v.encode('ascii')

    digest = sha256(sha256(v).digest()).digest()
    return b58encode(v + digest[:4])


def b58decode_check(v):
    '''Decode and verify the checksum of a Base58 encoded string.'''
    result = b58decode(v)
    result, check = result[:-4], result[-4:]
    digest = sha256(sha256(result).digest()).digest()

    if check != digest[:4]:
        raise ValueError("Invalid checksum")

    return result


def main():
    '''Base58 encode or decode FILE, or standard input, to standard output.'''
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument(
        'file',
        metavar='FILE',
        nargs='?',
        type=argparse.FileType('r'),
        default='-')
    parser.add_argument(
        '-d', '--decode',
        action='store_true',
        help='decode data')
    parser.add_argument(
        '-c', '--check',
        action='store_true',
        help='append a checksum before encoding')

    args = parser.parse_args()
    fun = {
        (False, False): b58encode,
        (False, True): b58encode_check,
        (True, False): b58decode,
        (True, True): b58decode_check
    }[(args.decode, args.check)]

    data = args.file.buffer.read()

    try:
        result = fun(data)
    except ValueError as e: # Catch Error
        sys.exit(e)

    if not isinstance(result, bytes):
        result = result.encode('ascii')

    sys.stdout.buffer.write(result)


if __name__ == '__main__':
    main()
