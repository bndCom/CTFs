- the binarty ELF 64-bit, simply when executed asks for user input and prints it
- once passed long string, segmentation fault happens, this means that the binary is vulnerable to **buffer overflow**, which can be confirmed with decompiling it using **Ghidra** for example, the size of the input's buffer is 64 byte, while the input length is <= 128 byte.

- Generally the main goal in such situation is exploiting this BOF to get a **shell** on the target system. How? by overwriting the function's return address and set it to the address of the function **system** within **libc**, and pass the argument "/bin/sh" for it.
The problem here is that we don't know this address because of **ASLR** (address space layout randomization), which changes the addresses of the libraries' modules each time the program is executed.
But something interesting is that the addresses of the dynamically linked functions are stored in the **GOT** (Global Offset Table).
So, to bypass ASLR, we need to leak that address from the GOT by exploiting the calls to function such as `printf` and `puts`

- after the leak, we can execute `system()` with "/bin/sh" as argument and get a shell

[solve script](./solve.py) does the job
