from pwn import *

p = remote("ctf.csd.lol", 5000)

p.recvuntil(b": ")
p.send(b"Leviev")
print(p.recv())
p.send(b"Microsoft")
print(p.recv())

p.interactive()
