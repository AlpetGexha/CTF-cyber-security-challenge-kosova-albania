import socket
import re
import time

# Function to decrypt Caesar cipher
def caesar_cipher_decrypt(text, key):
    shift = lambda c: chr((ord(c) - (65 if c.isupper() else 97) - key) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c
    return ''.join(shift(c) for c in text)

# Server details
host = "zhxjmxxhrj-ctf.cybersecuritychallenge.al"
port = 50000

while True:  # Keep trying until a flag is found
    try:
        print("Attempting to connect...")
        with socket.create_connection((host, port), timeout=5) as s:
            print("Connected to the server!")

            # Receive data from the server
            data = s.recv(1024).decode("utf-8")
            print("Raw Data Received:", repr(data))  # Debugging output

            if not data:
                print("No data received, retrying in 3 seconds...")
                time.sleep(3)
                continue

            # Match the encrypted string and key
            match = re.search(r"Encrypted string (.+) with key (\d+)", data)
            if match:
                encrypted_string = match.group(1)
                key = int(match.group(2))

                # Decrypt the string
                decrypted_string = caesar_cipher_decrypt(encrypted_string, key)
                print("Decrypted String:", decrypted_string)

                # Send the decrypted response
                s.sendall((decrypted_string + "\n").encode("utf-8"))
                print("Sent Response:", decrypted_string)

                # Check server's response
                server_response = s.recv(1024).decode("utf-8")
                print("Server Response:", repr(server_response))

                if "flag" in server_response.lower() or "congratulations" in server_response.lower():
                    print("Flag Found:", server_response)
                    break
            else:
                print("No task found. Server might have closed the connection.")
    except Exception as e:
        print("Connection Error. Retrying in 3 seconds...", e)
        time.sleep(3)