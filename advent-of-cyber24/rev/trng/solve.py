# given = A ^ (A >> 9)
#
# abcdefghijklmnopqrstuvwxyz -> i search for this
# XOR
# 000000000abcdefghijklmnopq
# =
# abcdefghi22222222222222222 -> i have this
# the idea is to find the first 9 bits of the secret, then xor each 9 bits of the given number with the previous 9 bits of the secret
# same for secret = secret ^ (secret << 7), only the direction is inversed (from right to left instead of left to right)
# # encryption for testing
# secret = 0x1938740263292304
# MASK = (1 << 64) - 1
# secret = secret ^ ((secret << 7) & MASK)
# given = secret ^ (secret >> 9)

from pwn import *

def decrypt_right_xorshift(given):
    given_bin = str(bin(given)[2:].zfill(64))
    result = given_bin[:9]
    for i in range(9, 64):
        next_bit = int(given_bin[i], 2) ^ int(result[i - 9], 2)
        result += str(next_bit)
    return int(result, 2)

def decrypt_left_xorshift(given):
    given_bin = str(bin(given)[2:].zfill(64))
    result = given_bin[57:64]
    for i in range(56, -1, -1):
        prev_bit = int(given_bin[i], 2) ^ int(result[6], 2) # + instead of -
        result = str(prev_bit) + result # concatenate from left
    return int(result, 2)

p = remote("kolmus.duckdns.org", 31337)
p.recvuntil(b"key: ")
p.sendline(b"trng")
p.recvuntil(b"iterations: ")
secret = int(p.recvline().split(b"x")[1].strip(), 16)
print(f"secret is: {hex(secret)}")

# decryption
for i in range(1000000):
    secret = decrypt_right_xorshift(secret)
    secret = decrypt_left_xorshift(secret)

p.recvuntil(b"(hex): ")
p.sendline(str(hex(secret)).encode())


p.interactive()

