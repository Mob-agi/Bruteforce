"""I've hidden some data using XOR with a single byte,
 but that byte is a secret. Don't forget to decode from
  hex first.
"""
Challenge = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
Soln = bytes.fromhex(Challenge)
for a in range(256):
    cipher = "".join(chr(a ^ b) for b in Soln)
    if cipher.startswith("crypto"):
        print(cipher)