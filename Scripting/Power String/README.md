```powershell
# Base64-encoded string
$encodedString = "76492d1116743f0423413b16050a5345MgB8AGMALwBjADEAUwAwADQATQBCADIAQgBqAGYANwBuAEkAZwBLAFoAWABoAHcAPQA9AHwANQA1ADIANgA1AGQAYwA0ADIANAA2ADIAOAA4ADEAOQA5ADgAZQBjADgAZgBiADEAYwBlAGQAMgBlADkAYQAxAGYAMwBiADEANABkADkAMgBmADAAYQBjAGEAYwBkADgAZQAwAGYANwA2AGUAYQA0ADQAYQAxADIAZgA3AGQANgA4ADUANgAwADQAYwAzADEAMwA3AGEAYQAwAGUAMABmAGUAYgBjADMAMgAwAGEAMQBkADQAYgBhADkAMgAxADYA"

# Key as a comma-separated string
$keyString = "3,4,2,3,56,34,254,222,1,1,2,23,42,54,33,233,1,34,2,7,6,5,35,43"

# Convert the key string into a byte array
$key = $keyString -split ',' | ForEach-Object { [byte]$_ }

# Convert the Base64-encoded string to a SecureString
$secureString = ConvertTo-SecureString -String $encodedString -Key $key

# Decode the SecureString to plain text
$decodedString = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureString))

# Output the decoded string
$decodedString
```