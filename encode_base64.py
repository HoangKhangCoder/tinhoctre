import base64

code = """
-.....   --.--..
"""

# Mã hóa 11 lần
encoded = code
for _ in range(10):
    encoded = base64.b64encode(encoded.encode()).decode()

print(encoded)