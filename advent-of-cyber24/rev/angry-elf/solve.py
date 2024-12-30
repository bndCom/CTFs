from pwn import xor

enc = bytes.fromhex("0f 0d 16 11 18 13 1a 0c 4f 46 5c".replace(" ", ""))
xor(enc, b"\x7f") # pringles09#
