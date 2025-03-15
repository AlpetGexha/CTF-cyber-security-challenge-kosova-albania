```python
def fix_zip_header(input_file: str, output_file: str):
    """
    Reads the input file and forces the first 4 bytes to be the correct ZIP signature.
    Writes the modified data to output_file.
    """
    try:
        with open(input_file, "rb") as f:
            data = f.read()
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    correct_signature = b"PK\x03\x04"
    # Replace the first 4 bytes with the correct signature.
    fixed_data = correct_signature + data[4:]
    
    try:
        with open(output_file, "wb") as f:
            f.write(fixed_data)
        print(f"[+] Fixed ZIP file written to '{output_file}'.")
        print("Now try extracting it using the password: CSC25")
    except Exception as e:
        print(f"Error writing {output_file}: {e}")

if __name__ == "__main__":
    # Original glitched file
    input_filename = "secret.zip"
    # This will be our fixed version.
    output_filename = "fixed_secret.zip"
    fix_zip_header(input_filename, output_filename)
```