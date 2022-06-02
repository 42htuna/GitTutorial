"""
Project description:
base58

Link:
https://pypi.org/project/base58/

İnstall:
pip install base58

Base58 and Base58Check implementation compatible with what is used by the bitcoin network.
Any other alternative alphabet (like the XRP one) can be used. Starting from version 2.0.0
python2 is no longer supported the 1.x series will remain supported but no new features
will be added.

Command line usage:
$ printf "hello world" | base58
StV1DL6CwTryKyV

$ printf "hello world" | base58 -c
3vQB7B6MrGQZaxCuFg4oh

$ printf "3vQB7B6MrGQZaxCuFg4oh" | base58 -dc
hello world

$ printf "4vQB7B6MrGQZaxCuFg4oh" | base58 -dc
Invalid checksum


Module usage:
>>> import base58
>>> base58.b58encode(b'hello world')
b'StV1DL6CwTryKyV'
>>> base58.b58decode(b'StV1DL6CwTryKyV')
b'hello world'
>>> base58.b58encode_check(b'hello world')
b'3vQB7B6MrGQZaxCuFg4oh'
>>> base58.b58decode_check(b'3vQB7B6MrGQZaxCuFg4oh')
b'hello world'
>>> base58.b58decode_check(b'4vQB7B6MrGQZaxCuFg4oh')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "base58.py", line 89, in b58decode_check
    raise ValueError("Invalid checksum")
ValueError: Invalid checksum
# Use another alphabet. Here, using the built-in XRP/Ripple alphabet.
# RIPPLE_ALPHABET is provided as an option for compatibility with existing code
# It is recommended to use XRP_ALPHABET instead
>>> base58.b58encode(b'hello world', alphabet=base58.XRP_ALPHABET)
b'StVrDLaUATiyKyV'
>>> base58.b58decode(b'StVrDLaUATiyKyV', alphabet=base58.XRP_ALPHABET)
b'hello world'
"""

import base58

seed = b'hello world'
encoded_seed = base58.b58encode(seed)
print(encoded_seed)
