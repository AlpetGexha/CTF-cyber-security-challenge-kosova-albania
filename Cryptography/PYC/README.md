```bash
└─# strings secret.py        
# uncompyle6 version 3.9.2
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.11.8 (main, Feb  7 2024, 21:52:08) [GCC 13.2.0]
# Embedded file name: secret.py
# Compiled at: 2025-02-26 08:31:19
# Size of source mod 2**32: 795 bytes
import base64
a = "Vm10a01GVXhVbk5pTTJSUFZteGFWb"
b = "FpxU2xOVlJsWnlWbGhvYVdKR1NscFpNRlozV1ZV"
c = "eFJWSlVTbGRpUjFKeV"
d = "ZrUkJlRkp0U2toT1ZsWnBZbXRLV0ZZeWNFSk5WMDV6VjJ4b1lWSlViRzl"
e = "aV0hCSFpGWmFTRTFVUWxoaVJ6a3pWR3hvUzFac1dYbFZiRU"
f = "poVmpOU1NGbHRlRk5rVjA1SlUyMUdUbEpHV2pWV2ExcHJZVEZSZVZKdVRsZGlWRlpXV1d0YVlWbFdaSEZSV0doUFlrWmFXVmRy"
g = "VlRWV01WcDBaVWhXVjFKNlZqTldWM"
k = "2gyWkRBMVdWS"
j = "nRSazVpVmtwUVYyeGtlbVZIU25OVmJrNVhZa2hDYUZSVlVsWk5iR1JWVTIxMFZXSldXbmxXYlRBeFZsZEtXVlZzWkZoaGEwVjNXa1JHVjFaVk1VV"
h = "k5SREE5"
pointer = 0
string = ""
while pointer < 6:
    string = base64.b64decode(a + b + c + d + e + f + g + k + j + h).decode()
    pointer += 1
print(flag)



CSC25{uncompyle_4_th3_w1n}

```