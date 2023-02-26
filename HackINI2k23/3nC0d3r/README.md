## What we’ve got?

So we have `prog`  which is ELF 64 bits binary file and `flag_encoded` file.

When running the program it asks for a file name: if we enter an existing file name it will make new file named `flag_encoded_encoded`, else it generates `flag_encoded_binary` file. We understand that our program is encoding files, so we'll discover how it is going to decrypt `flag_encoded` file.

## Solution:

### Encryption:

After analysing and cleaning the program’s code using Ghidra, the program is essentially built in two parts; the first makes the binary file and the second the encoded file, but the binary is disappearing once the program ends, here we’ll use (gdb) to debug the program and make breakpoint at the instruction of removing it (binary file) so we can get it and ensure our good understanding for the program.

The program is working this way: 

- First part: for each character in the flag file it converts it to binary ascii and it adds zeros to it (from left) to complete 8bits (’A’=65 → 1000001 → **0**1000001).
- Second part: in the code we have two characters lists:
    
    `ZeroList[] = {’A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H'}`
    
    `OneList[] = {’I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'P' , 'Q'}`
    
    the lists names explain their role, lets make things clear:
    
    - with every change in the binary digits (from ‘0’ to ‘1’ or ‘1’ to ‘0’) the program puts a character in the `flag_encoded_encoded` file, the character is token from the first digit list ( 01 → we take char from `ZeroList[]` , 10 → `OneList[]`) and the index of the char in the list is the successive repetition of the first digit -1 for example:
        
        ‘A’ = 01000001 , the first change in digits is **01**000001, the first digit is ‘0’ and it’s repeated one time  so we take `ZeroList[1-1=0]='A'` , then in 0**10**00001 the char is `OneList[1-1=0]=’I’` then in 010000**01** we take `ZeroList[5-1=4]=’E’` and so on until the end of binary file so we get the `flag_encoded_encoded` file.
        

### Decryption:

Here we have the `flag_encoded` file, we’ll try to decrypt it in two part:

- First part: we’ll generate the binary file as follows: for each character in `flag_encoded`, if it’s in the `ZeroList[]` we append the binary file with ‘0’ n times (’n’ is the index of the char in the List + 1), the same if the digit is ‘1’ (`OneList[]`).
- Second part: after getting the binary file from part1, with each successive 8 bits in it we convert them to ASCII Base10 then into bytes to get our `flagFile`.

we notice that `flagFile` is GIF file so we can run it with any image viewer to say welcome to our flag `/***shellmates{h0w_d1D_YOu_br34K_mY_3nc0d1nG?}*/`.**

**NOTE:** all the files and scripts are attached with this repo.
