import base64
import binascii
from codecs import decode as rot13_decode

def decode_layers(encoded_message):
    while True:
        try:
            # Attempt Base64 decoding
            try:
                decoded_message = base64.b64decode(encoded_message).decode()
                print(f"Base64 Decoded: {decoded_message}")
                encoded_message = decoded_message
                continue
            except (binascii.Error, UnicodeDecodeError):
                pass

            # Attempt ROT13 decoding
            try:
                decoded_message = rot13_decode(encoded_message, 'rot_13')
                print(f"ROT13 Decoded: {decoded_message}")
                encoded_message = decoded_message
                continue
            except Exception:
                pass

            # Attempt hexadecimal decoding
            try:
                decoded_message = bytes.fromhex(encoded_message).decode()
                print(f"Hex Decoded: {decoded_message}")
                encoded_message = decoded_message
                continue
            except (ValueError, UnicodeDecodeError):
                pass

            # If no more decodings work, stop
            print("No further decoding possible.")
            break

        except Exception as e:
            print(f"An error occurred: {e}")
            break

        # Check for the flag
        if "flag" in encoded_message.lower():
            print(f"Flag found: {encoded_message}")
            break

# Replace this with your encoded message
encoded_message = "D1AQZwI7GIIfIQSsGQE5Z3WsZ25wZTDkozq9"

decode_layers(encoded_message)
