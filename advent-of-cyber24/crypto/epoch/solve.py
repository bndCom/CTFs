from pwn import *
import base64

p = remote("backup.csd.lol", 5002)
p.recv()
p.sendline(b"2")
flag = unhex(p.recv())
print(flag)
# dec from xor
epc = str(int(time.time())).encode()
half_dec = xor(flag, epc)
print(epc)
print(half_dec.decode())
half_dec2 = base64.b64decode(half_dec)

# dec final
full_dec = bytes([(b - 3) % 256 for b in half_dec2])
print(full_dec)

p.interactive()