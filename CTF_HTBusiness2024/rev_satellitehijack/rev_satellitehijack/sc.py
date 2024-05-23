enc = "l5{0v0Y7fVf?u>|:O!|Lx!o$j,;f"

for i in range(len(enc)):
    print(chr(ord(enc[i]) ^ i), end="")
