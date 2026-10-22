import base64

SECRET_KEY = "LEAKED123"
RAW_DATA_STRING = """
PASTE YOUR GIANT RAW TEXT OR JSON DATA HERE
"""

# Scramble the characters
scrambled = "".join(chr(ord(c) ^ ord(SECRET_KEY[i % len(SECRET_KEY)])) for i, c in enumerate(RAW_DATA_STRING.strip()))
safe_string = base64.b64encode(scrambled.encode('utf-8')).decode('utf-8')

# Save directly as a plain text string
with open("MtxShit.txt", "w", encoding="utf-8") as f:
    f.write(safe_string)

print("Success! Created MtxShit.txt")
