import base64
from Crypto.Cipher import AES

def remove_pkcs7_padding(data: bytes) -> bytes:
    """
    Removes PKCS#7 padding from the decrypted data.
    """
    padding_len = data[-1]
    if padding_len < 1 or padding_len > AES.block_size:
        # No valid padding found; return data as is.
        return data
    return data[:-padding_len]

def main():
    # Read in the ciphertext from ciphertext.txt and the key from password.txt
    with open("ciphertext.txt", "r") as f:
        ciphertext_b64 = f.read().strip()
    with open("password.txt", "r") as f:
        key = f.read().strip().encode()  # key should be 16 bytes for AES-128

    # Convert the base64 ciphertext into raw bytes
    try:
        ciphertext = base64.b64decode(ciphertext_b64)
    except Exception as e:
        print("Base64 decode error:", e)
        return

    # Create an AES cipher in ECB mode using the key
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the ciphertext
    decrypted = cipher.decrypt(ciphertext)

    # Remove padding (if PKCS#7 padding was used)
    decrypted = remove_pkcs7_padding(decrypted)

    try:
        plaintext = decrypted.decode("utf-8")
    except UnicodeDecodeError:
        plaintext = decrypted.decode("utf-8", errors="replace")

    print("Recovered plaintext:")
    print(plaintext)

if __name__ == "__main__":
    main()
