```python
ciphertext = bytes.fromhex("000000000549622b631c03436d6d3b0b3b6a0040723e")
key = b"CSC2025"

# Decrypt with repeating XOR
plaintext = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])
print("Plaintext:", plaintext.decode())
```