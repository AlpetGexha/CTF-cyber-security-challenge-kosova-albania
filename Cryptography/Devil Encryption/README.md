```python
def devils_encrypt(text, key):
    encrypted_text = ""
    key = key.lower()
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text
def devils_decrypt(encrypted_text, key):
    decrypted_text = ""
    key = key.lower()
    key_index = 0
    key_length = len(key)

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

# Example usage
encrypted_flag = "RJG25{g0xY1nv_sYm_4_hI34m}"
key = "pretera"
decrypted_flag = devils_decrypt(encrypted_flag, key)
print("Decrypted Flag:", decrypted_flag)
```
